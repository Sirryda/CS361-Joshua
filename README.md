Assignment Title:
S2.6 - Assignment 9: Microservice Implementation (Milestone #2) + Publish Communication Contract to Partner

Description:
Add a README to your GitHub (or update it if you already have one) that contains your communication contract. (Once you define it, don't change it! Your partner is relying on you.) README must contain...
    A.	Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.
    B.	Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.
    C.	UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your partner (and your grader)             will understand

Microservice:
The Microservice will take the user command from the stock_insight_cli.py to create, add, delete or view a watchlist. The watchlist information will be saved to microservice.txt file stored in the same folder as the stock_insight_cli.py and the app.py. When adding a stock to watchlist.txt file, the microservice will get the current price from the AlphaVantage API and then add it to the file.

Executing the program:

<b>Requesting Data:</b>
   
<b>Add to Watchlist:</b>
- User will type “add-to-watchlist” at the prompt.
- The screen will then ask for the stock symbol for a stock to be added.
  
    ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/84958d37-51d5-406d-9687-5864c71b3902)
- Once the user types a stock (AAPL for example), the program will send a POST request to ‘/add_to_watchlist’ with a JSON payload with         the ‘symbol’ (as a string) and ‘price’ (as a number). This can take up to a few seconds.
- The program will get the price from “def get_current_price(self, symbol)”.
- If successful, a confirmation message will be printed.
  
  ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/a805ed56-b866-4895-a315-023b1ee4190b)
- If not successful, a message saying the stock was not added will print.
 
![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/1d03f899-62cf-4efb-ac2d-13091615adb1)

<br>
<br>

<b>To View the Watchlist:</b>

- User will type “watchlist” at the prompt.
- The program will send a GET request to ‘/view_watchlist”.
- If there are stocks stored in watchlist.txt file, it will print a JSON array containing the stocks in the watchlist with ‘symbol’ (as a string) for the stock symbol and ‘price’ (as a number) for the price that was stored in the file.
- If there are stocks stored in watchlist.txt, it will print the symbol and price for stocks stored.
  ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/af6c38d7-e94f-47c2-8856-28eca827cb97)
- If no stocks are stored in watchlist.txt file, it will return with an empty list.  
  ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/2fc5f70b-7672-41c7-98af-416c9108f8c2)
- The program will ask for a new command from the user.
<br>
<br>
<b>Receiving Data:</b>
<br>
<b>Add to Watchlist:</b>

- The program will use def get_current_price(self, symbol) to GET the current price for the stock the user wants to add.
- Once the stock has been added to the watchlist, the program will print a confirmation message. This will show the user that the stock was added successfully.
- If the stock was typed incorrectly, it will print the error message.

<br>
<b>Watchlist:</b>

- When viewing the watchlist, the user will receive a JSON array that contains the stocks and prices that are saved in the watchlist.txt file.
- The program will print the stocks from the watchlist.txt, which include the ‘symbol’ (as a string) and ‘price’ (as a number).



![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/d3d7a563-0601-4d2e-adbe-c06cbe985e47)
