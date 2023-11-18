import requests
import os


class StockInsightCLI:
    # Diana - Added the WATCHLIST_FILE_PATH information. Also added the import os above
    def __init__(self):
        self.base_url = 'http://localhost:5000/'
        self.WATCHLIST_FILE_PATH = 'watchlist.txt'
        if not os.path.exists(self.WATCHLIST_FILE_PATH):
            with open(self.WATCHLIST_FILE_PATH, 'w'):
                pass 

    # Diana - Watchlist Handle
    def handle_watchlist(self):
        print("Your watchlist:")
        try:
            with open(self.WATCHLIST_FILE_PATH, 'r') as file:
                watchlist_data = file.readlines()
                for line in watchlist_data:
                    symbol, price = line.strip().split()
                    print(f"Symbol: {symbol}, Price: {price}")
        except FileNotFoundError:
            print("Watchlist file not found. It seems you haven't added any stocks yet.")
        except Exception as e:
            print(f"An error occurred while reading the watchlist: {e}")

    # Diana - Adds the stock to the watchlist
    def add_to_watchlist(self, symbol):
        try:
            current_price = self.get_current_price(symbol)
            if current_price is not None:
                current_price = round(float(current_price), 2)
                self.add_to_watchlist_file(symbol, current_price)
                print(f"{symbol} added to your watchlist with the current price: {current_price}")
            else:
                print(f"Could not add {symbol} to watchlist.")
        except Exception as e:
            print(f"An error occurred while adding {symbol} to watchlist: {e}")

    # Diana - Add to watchlist file
    def add_to_watchlist_file(self, symbol, current_price):
        with open(self.WATCHLIST_FILE_PATH, 'a') as file:
            file.write(f"{symbol} {current_price}\n")

    # Diana - Removes the stock from the watchlist
    def remove_from_watchlist(self, symbol):
        try:
            with open(self.WATCHLIST_FILE_PATH, 'r') as file:
                watchlist_data = file.readlines()
            
            with open(self.WATCHLIST_FILE_PATH, 'w') as file:
                for line in watchlist_data:
                    if symbol not in line:
                        file.write(line)

            print(f"{symbol} removed from your watchlist.")
        except FileNotFoundError:
            print("Watchlist file not found. It seems you haven't added any stocks yet.")
        except Exception as e:
            print(f"An error occurred while removing {symbol} from the watchlist: {e}")

    # Diana - Handle to remove stock from watchlist
    def handle_remove_from_watchlist(self):
        symbol = input("Enter the stock symbol to remove from watchlist: ").strip().upper()
        self.remove_from_watchlist(symbol)

    def get_current_price(self, symbol):
        # Diana - Gets the current price of a stock from Alpha Vantage
        api_key = 'S4U9D9FVFLIA63BF'
        alpha_vantage_url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'

        try:
            response = requests.get(alpha_vantage_url)
            response.raise_for_status()
            data = response.json()

            if 'Global Quote' in data:
                return data['Global Quote']['05. price']
            else:
                print(f"Could not retrieve current price for {symbol}.")
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'An error occurred: {err}')
        return None
    ##########################
    # Diana - End of my microservice.
    ##########################

    def fetch_stock_data(self, endpoint, params):
        try:
            response = requests.get(f'{self.base_url}{endpoint}', params=params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'An error occurred: {err}')
        return None

    def handle_top_stocks(self):
        print("Fetching top-performing stocks...")
        data = self.fetch_stock_data('top_stocks', {})
        if data:
            top_gainers = data[:5]  # Get the top 5 gainers
            print("Top 5 gainers:")
            for stock in top_gainers:
                self.display_stock_info(stock)
        else:
            print("Could not retrieve data.")

    def handle_bottom_stocks(self):
        print("Fetching bottom-performing stocks...")
        data = self.fetch_stock_data('bottom_stocks', {})
        if data:
            top_losers = data[:5]  # Get the top 5 losers
            print("Top 5 losers:")
            for stock in top_losers:
                self.display_stock_info(stock)
        else:
            print("Could not retrieve data.")

    def handle_daily_open_close(self):
        symbol = input("Enter the stock symbol (e.g., AAPL for Apple): ").strip().upper()
        print(f"Fetching the most recent open and close prices for {symbol}...")
        data = self.fetch_stock_data('daily_open_close', {'symbol': symbol})
        if data:
            print(f"Date: {data['date']}, Open: {data['open']}, Close: {data['close']}")
        else:
            print("Could not retrieve data.")

    # TODO: Implement news functionality

    # TODO: Implement alerts functionality

    def display_stock_info(self, stock):
        print(f"Ticker: {stock['ticker']}, Price: {stock['price']}, Change Percentage: {stock['change_percentage']}")

    # Diana - Added Watclist, add-to-watchlist, and remove-from-watchlist to main commands
    def display_welcome_message(self):
        welcome_message = '''
--------------------------
|  StockInsight CLI v1.0 |
--------------------------
Welcome to StockInsight CLI! Your one-stop solution for real-time financial market insights.

Dive into the financial market with live data, from top-performing stocks to critical 
trading alerts, all at your fingertips.

Main Commands:
  - top-stocks: View top-performing stocks
  - bottom-stocks: View lowest-performing stocks
  - daily-open-close: Get the most recent open and close prices for a stock
  - alerts: Set up trading alerts
  - watchlist: View your watchlist
  - add-to-watchlist: Add a stock to your watchlist
  - remove-from-watchlist: Remove a stock from your watchlist
  - news: Access the latest financial news
  - help: List all commands with descriptions
  - exit: Exit the application
'''
# TODO: Add new commands to welcome prompt

        print(welcome_message)

    def run(self):
        self.display_welcome_message()

        while True:
            command = input("\nPlease enter a command (type 'help' for options): ").strip().lower()

            if command == 'exit':
                print("Exiting StockInsight CLI. Goodbye!")
                break

            elif command == 'top-stocks':
                self.handle_top_stocks()

            elif command == 'bottom-stocks':
                self.handle_bottom_stocks()

            elif command == 'daily-open-close':
                self.handle_daily_open_close()

            elif command == 'watchlist':
                self.handle_watchlist()
            
            elif command == 'add-to-watchlist':
                symbol = input("Enter the stock symbol: ").strip().upper()
                self.add_to_watchlist(symbol)

            elif command == 'remove-from-watchlist':
                self.handle_remove_from_watchlist()

            elif command == 'help':
                self.display_command_help()

            else:
                print(f"Unknown command: {command}. Please type 'help' for options.")

    def display_command_help(self):
        # Display available commands
        
        # Diana - Added Watclist, add-to-watchlist, and remove-from-watchlist to help message
        help_message = {
            'top-stocks': 'View top-performing stocks',
            'bottom-stocks': 'View lowest-performing stocks',
            'daily-open-close': 'View the most recent open and close prices for a given symbol',
            'watchlist': 'View your watchlist',
            'add-to-watchlist': 'Add a stock to your watchlist',
            'remove-from-watchlist': 'Remove a stock from your watchlist',
            # TODO: Add new commands here
        }
        print("Available commands:")
        for cmd, description in help_message.items():
            print(f'  - {cmd}: {description}')


if __name__ == "__main__":
    stock_insight_cli = StockInsightCLI()
    stock_insight_cli.run()