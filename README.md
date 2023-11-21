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
Requesting Data:
1.	User needs to open the 2 python programs named app.py and stock_insight_cli.py in the user’s IDE or programs.
2.	The onscreen message will show. There are 3 commands that I had added: “watchlist”, “add-to-watchlist” and “remove-from-watchlist”.
   ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/df852a81-8b0c-46ed-acf2-210b35d6ef17)
•	 Add to Watchlist:
    o	User will type “add-to-watchlist” at the prompt.
    o	The screen will then ask for the stock symbol for a stock to be added.
      ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/84958d37-51d5-406d-9687-5864c71b3902)
    o	Once the user types a stock (AAPL for example), the program will send a POST request to ‘/add_to_watchlist’ with a JSON payload with         the ‘symbol’ (as a string) and ‘price’ (as a number). This can take up to a few seconds. 
    o	The program will get the price from “def get_current_price(self, symbol)”.
    o	If successful, a confirmation message will be printed.
     ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/a805ed56-b866-4895-a315-023b1ee4190b)
    o	If not successful, a message saying the stock was not added will print.
     ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/d2e4cab7-04cd-4971-8d66-f1c5c34677ff)

    o	After either successful or unsuccessful messages, it will ask for a new command.

•	Remove from Watchlist:
    o	User will type “remove-from-watchlist” at the prompt.
    o	The screen will ask for the stock symbol to be removed from watchlist.
     ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/6d065754-ed15-4f8c-a784-b8a1f29032ad)
    o	Once the user types a stock (AAPL for example), the program will send a POST request to ‘/remove_from_watchlist’ with a JSON payload with ‘symbol’ (as a string). This can take a few seconds.
    o	A message saying the stock as been removed from watchlist will be shown.
     ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/37b705b9-5b20-4715-8738-8ad0f74046cf)
    o	The program will ask for a new command from the user.

•	To View the Watchlist:
    o	User will type “watchlist” at the prompt.
    o	The program will send a GET request to ‘/view_watchlist”.
    o	If there are stocks stored in watchlist.txt file, it will print a JSON array containing the stocks in the watchlist with ‘symbol’ (as a string) for the stock symbol and ‘price’ (as a number) for the price that was stored in the file.
    o	If there are stocks stored in watchlist.txt, it will print the symbol and price for stocks stored.
     ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/af6c38d7-e94f-47c2-8856-28eca827cb97)
    o	If no stocks are stored in watchlist.txt file, it will return with an empty list.  
    ![image](https://github.com/Sirryda/CS361-Joshua/assets/1214872/2fc5f70b-7672-41c7-98af-416c9108f8c2)
    o	The program will ask for a new command from the user.

Receiving Data:
•	Add to Watchlist:
    o	The program will use def get_current_price(self, symbol) to GET the current price for the stock the user wants to add.
    o	Once the stock has been added to the watchlist, the program will print a confirmation message. This will show the user that the stock was added successfully.
    o	If the stock was typed incorrectly, it will print the error message.

•	Remove from Watchlist:
    o	Once the user types the stock symbol that should be removed, the program will print a confirmation messaging saying it was removed.          This will happen even if the stock symbol typed isn’t in the list since it will no longer be on the watchlist.txt file.


•	Watchlist:
    o	When viewing the watchlist, the user will receive a JSON array that contains the stocks and prices that are saved in the watchlist.txt file.
    o	The program will print the stocks from the watchlist.txt, which include the ‘symbol’ (as a string) and ‘price’ (as a number).
