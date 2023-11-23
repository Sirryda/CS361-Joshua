from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

WATCHLIST_FILE_PATH = 'watchlist.txt'

def get_current_price(symbol):
    """Fetch the most recent close price for a given symbol."""
    function = "TIME_SERIES_DAILY"
    alpha_vantage_url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={alpha_vantage_api_key}'

    try:
        response = requests.get(alpha_vantage_url)
        response.raise_for_status()
        data = response.json()

        if 'Time Series (Daily)' not in data:
            print(f"No 'Time Series (Daily)' data found for symbol: {symbol}")
            return None

        recent_date = list(data['Time Series (Daily)'].keys())[0]
        recent_data = data['Time Series (Daily)'][recent_date]

        return recent_data['4. close']
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred while fetching price for {symbol}: {http_err}')
        return None
    except Exception as err:
        print(f'Error fetching current price for {symbol}: {err}')
        return None

@app.route('/add_to_watchlist', methods=['POST'])
def add_to_watchlist():
    try:
        data = request.get_json()
        symbol = data.get('symbol')
        price = data.get('price')

        if symbol and price:
            current_price = get_current_price(symbol)
            if current_price is None:
                return jsonify({'error': 'Failed to fetch current stock price'}), 500
            # Check if the watchlist file exists
            if not os.path.exists(WATCHLIST_FILE_PATH):
                with open(WATCHLIST_FILE_PATH, 'w') as file:
                    file.write(f"{symbol} {price}\n")
            else:
                with open(WATCHLIST_FILE_PATH, 'a') as file:
                    file.write(f"{symbol} {price}\n")

            return jsonify({'message': 'Stock added to watchlist successfully',
                            'current_price': current_price
            })
        else:
            return jsonify({'error': 'Symbol and price are required parameters'}), 400
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

@app.route('/view_watchlist', methods=['GET'])
def view_watchlist():
    try:
        # Check if the watchlist file exists
        if os.path.exists(WATCHLIST_FILE_PATH):
            with open(WATCHLIST_FILE_PATH, 'r') as file:
                watchlist_data = [line.strip().split() for line in file.readlines()]

            watchlist = [{'symbol': item[0], 'price': item[1]} for item in watchlist_data]
            return jsonify({'watchlist': watchlist})
        else:
            return jsonify({'watchlist': []})
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)