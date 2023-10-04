# Crypto Wallet
![Litecoin_image](https://github.com/Happa1/unit1-2024/assets/142579414/535df8e1-343f-417c-a2eb-12f063ad84b0)
**Fig.1**
What is litecoin?| CMC Markets

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all her transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms. Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

An example of the data stored is 

| Date | Description | Category | Amount  |
|------|-------------|----------|---------|
| Sep 23 2022 | bought a house | Expenses | 10 BTC |
| Sep 24 2022 | food for house celebration | Food | 0.000001 BTC |


## Proposed Solution

Design statement:
I will to design and make an electronic ledger for a client who is Ms.Sato. 
The electronic ledger will about the system which records transaction of cryptocurrency and display clear profit and exchange. 
It is constructed by using the software, "PyCharm" and programming language, Python. It will take 3 weeks to make it and will 
be evaluated according to the success criteria below.

## Description of the coin
Litecoing is the second-oldest cryptoncurrency created from a fork in the Bitoboin blockchain in 2011 by former Google engineer Charlie Lee. Litecoin was released with 150 pre-mined coins and has a total supply of 84 million coins, and its blockchain generates a new block every 2.5 minutes. A new hashing algorithm allows to reduce over time to preserce the coin's value and faster transaction speeds.

**Citation**

“Litecoin (LTC): What It Is, How It Works, vs. Bitcoin.” Investopedia, 2023, www.investopedia.com/articles/investing/040515/what-litecoin-and-how-does-it-work.asp. Accessed 12 Sept. 2023.

Napoletano, E. “What Is Litecoin? How Does It Work?” Forbes, 30 Jan. 2023, www.forbes.com/advisor/investing/cryptocurrency/litecoin/. Accessed 12 Sept. 2023.

## Tools of my solution
I decided to use python this time because it is the most common language in programming, so that she can understand the code easily and other developers will be able to improve my program in the future. I also used Pycharm to develop this program because it has a good UI and many funtion to indicate possible error occurs to prevent the code from messing up.
To accomplish the client's requirements, I imported pands, time, textwrap, datetime, and matplotlib.pyplot libraries, and also used csv file to record user data and transaction data. These libraries allowed me to make advanced program without complicated codes, and csv file makes it easy to create, read, and edit it.

**Citation**

upGrad. “Top 12 Commerce Project Topics & Ideas in 2023 [for Freshers].” UpGrad Blog, upGrad Education, 28 Sept. 2022, www.upgrad.com/blog/reasons-why-python-popular-with-developers/. Accessed 4 Oct. 2023.

‌“Is Python Good for Software Development? - BairesDev Blog: Insights on Software Development & Tech Talent.” BairesDev Blog: Insights on Software Development & Tech Talent, 22 June 2022, www.bairesdev.com/blog/is-python-good-for-software-development/. Accessed 4 Oct. 2023.

‌alexandre. “PyCharm: All about the Most Popular Python IDE.” Data Science Courses | DataScientest, 20 Feb. 2023, datascientest.com/en/pycharm-all-about-the-most-popular-python-ide#:~:text=The%20main%20advantages%20of%20PyCharm,error%20highlighting%20improves%20the%20process. Accessed 4 Oct. 2023.

Simpson, Scott. “Why Use a Database? - Programming Foundations: Databases.” LinkedIn, 28 Mar. 2019, www.linkedin.com/learning/programming-foundations-databases-2/why-use-a-database#:~:text=%2D%20Databases%20let%20us%20work%20with,they%20help%20us%20avoid%20redundancy. Accessed 4 Oct. 2023.


## Structure of my solution
To ensure the security of electronic ledger, I want to create a system of singup, login, and logout. I also want to create function of deposit, withdrawal, balance, transaction table, and chart to make it easier for the client to use electroni ledger and show her transaction visually through table and line graph.
I specified those structures in the success criteria below.

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger has sign up, log in, and log out system.
5. The electronic ledger allows to enter, withdraw and record transactions.
6. The electronic ledger display the exchange of currency (yen and dollars).
7. The electronic ledger display profit after user enter or withdraw cryptocurrency.
8. The electronic ledger display the line graph of transaction and profit.

# Criteria B: Design

## System Diagram
![Computer Science quiz (4)](https://github.com/Happa1/unit1-2024/assets/142579414/cc52062e-6ac4-4541-8b2b-44914819d82e)
**Fig. 2** This is the System Diagram of the project with starts from input by keyboard, and ends with output by display of the computer. I developed my project in wallet.py file with user.csv file and user's own atm csv files in pycharm. I also import the LTC echange rate data from the Internet, the citation is listed below.

## Flow Diagrams
![Computer Science quiz (1)](https://github.com/Happa1/unit1-2024/assets/142579414/887dacb9-3997-4dcc-9d05-15b9e288494c)
**Fig. 3** This is the flow diagram for the singup system. This summarizes how the singup system works.

![Computer Science quiz (2)](https://github.com/Happa1/unit1-2024/assets/142579414/c9a8b4af-7d4b-47be-be5e-efc1d638854b)
**Fig. 4** This is the flow diagram for the login system. This summarizes how the login system works.

![Computer Science quiz (3)](https://github.com/Happa1/unit1-2024/assets/142579414/f34b93d3-4d26-4248-9ea5-c1d58f060638)
**Fig. 5** This is the flow diagram for the deposit system. This summarizes how the deposit system works.


## Record of Tasks
| Task No | Planned Action                                        | Planned Outcome                                                                                                                  | Time estimate | Target completion date | Criterion |
|---------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Decide crypto currency which I use                    | To decide what type of crypto currency I use in this project.                                                                    | 10 min        | Sep 11                 | A         |
| 2       | Write a description about LTC                         | To understand the crypto currency which I use in this project, and to create a currency description to use it in code.           | 20 min        | Sep 12                 | A         |
| 3       | Create system diagram                                 | To have a clear idea of the hardware and software requirements for the proposed solution.                                        | 15min         | Sep 13                 | B         |
| 4       | Create a login System                                 | To have a flow diagram and the code for the login system.                                                                        | 30min         | Sep 14                 | B, C      |
| 5       | Create a success Criteria with design statement       | To have approved success criteria and write a design statement.                                                                  | 20min         | Sep 18                 | B         |
| 6       | Crate deposit system                                  | To have a deposit function by using CSV data.                                                                                    | 20min         | Sep 20                 | C         |
| 7       | Create withdrawal system                              | To have a withdrawal function by using CSV data.                                                                                 | 10min         | Sep 20                 | C         |
| 8       | Create balance system                                 | To have a function to calculate the balance from deposit and withdrawal data.                                                    | 10min         | Sep 20                 | C         |
| 9       | Create validated integer function                     | To have a function to validate integers to prevent the error from occurring.                                                     | 10min         | Sep 20                 | C         |
| 10      | Create signup system                                  | To have a signup function by using a username and password, and record it in the user cv file.                                   | 20min         | Sep 29                 | C         |
| 11      | Peer feedback (May, Marina, Agatha, Rocky)            | To get and give feedback each other to improve the project.                                                                      | 20min         | Sep 29                 | A,B       |
| 12      | Create transaction table                              | To get a data of transaction from CSV data and display it.                                                                       | 30min         | Sep 29                 | C         |
| 13      | Adjust the width of currency description              | To have a good width of description which fits the display of the computer.                                                      | 10min         | Sep 29                 | C         |
| 14      | Create mark down transaction table                    | To get a mark down table for transaction history.                                                                                | 10min         | Sep 29                 | C         |
| 15      | Create currency exchange function                     | To get live data of LTC price and show exchanged price in both $ and ¥.                                                          | 80min         | Sep 29                 | C         |
| 16      | Create menu function                                  | To have a function to display a menu with a short code.                                                                          | 10min         | Sep 29                 | C         |
| 17      | Create menu loop                                      | To have a function to show menu after one session ends.                                                                          | 10min         | Sep 29                 | C         |
| 18      | Create validated integer error message function       | To have a function to show an error message depending on the error the client makes.                                             | 5min          | Sep 29                 | C         |
| 19      | Create function to clarify debt                       | To have a function to identify the client is whether debt or not after she deposit or withdrawal.                                | 5min          | Sep 29                 | C         |
| 20      | Create time sleep function                            | To have a pause between each session so that client can take time to see descriptions.                                           | 5min          | Sep 29                 | C         |
| 21      | Add citation for description                          | To have a citation for the currency description with good UI.                                                                    | 5min          | Sep 30                 | C         |
| 22      | Create balance function                               | To have a function to calculate balance.                                                                                         | 15min         | Sep 30                 | C         |
| 23      | Create line graph of deposit, withdrawal, and balance | To have a line graph which shows history of deposit, withdrawal, and balance, and client can choose the graph she wants to fraw. | 50min         | Sep 30                 | C         |
| 24      | Improve CSV data table                                | To have a CSV data with column of date, description, category, amount, and balance.                                              | 30min         | Oct 1                  | C         |
| 25      | Create log out function                               | To have a log-out function to exit from logged-in status safely.                                                                 | 20min         | Oct 1                  | C         |
| 26      | Create end menu                                       | To have a function to show the menu.                                                                                             | 10min         | Oct 1                  | C         |
| 27      | UI design of project overall                          | To have an adequate pause between each session, clear visual, and good color.                                                    | 15min         | Oct 1                  | B         |

## Testing plan
| Test                         | Type               | Process (input)                                                                                                                                                                                                                                    | Expected output                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User Signup                  | Unit testing       | 1. Choose 1 as a signup option (1) 2. Enter a username. (mano) 3. Enter a password. (1357) 4. Enter a confirmation password. (1357)                                                                                                                | If the username is not used already sign upped users,  and the password and a confirmation password match,  record the username and the password in the csv file. If the user successfully can sign up, the login menu is displayed.                                                                                                                                                                                                |
| User Login                   | Unit testing       | 1. Enter a username. (mano) 2. Enter a password. (1357)                                                                                                                                                                                            | If the username and the password that the user entered match with the  data on the csv file of user data, the user successfully logged in.                                                                                                                                                                                                                                                                                          |
| Validate the Integer of menu | Unit testing       | 1. Enter the number depending on the menu the user chooses. (1 or 2 or 3 or 4 or 5 or 6)                                                                                                                                                           | If the thing that the user entered is an integer and either one of the numbers in menu, program move on to the session depending on the number the user chooses.                                                                                                                                                                                                                                                                    |
| Deposit                      | Unit testing       | 1. Choose deposit in menu (1). 2. Enter a description of the deposit. (food) 3. Enter the amount of the deposit. (150)                                                                                                                             | If the user enter description and the amount in integer, date, description, deposit(category), amount, balance is recorded in the user's own atm csv file. If the deposit system is successfully done, it displays "Saved" and shows the balance that the user currently has. Also, if the balance is bigger than 0, it displays "You're not debt", and if it is below 0, displays "You're debt"                                    |
| Currency exchange            | Unit testing       | 1. Choose either us dollar or Japanese yen and enter  the choice in integer (1 or 2)                                                                                                                                                               | If the user enter her currency exchange option in integer in 1 or 2, the currency exchange starts. If the user chooses us dollar, get the LTC price in us dollar and multiply with balance, and displays it. If the user chooses Japanese dollar, get the LTC price in Japanese dollar and multiply with balance, and displays it.                                                                                                  |
| Withdrawal                   | Unit testing       | 1. Choose withdrawal in menu (2). 2. Enter a description of the withdrawal. (house) 3. Enter the amount of the deposit. (200)                                                                                                                      | If the user enter description and the amount in integer, date, description, withdrawal(category), amount, balance is recorded in the user's own atm csv file. If the withdrawal system is successfully done, it displays "Saved" and shows the balance that the user currently has. Also, if the balance is bigger than 0, it displays "You're not debt", and if it is below 0, displays "You're debt"                              |
| Balance                      | Unit testing       | 1. Choose balance in menu (3).                                                                                                                                                                                                                     | By reading the user's own atm csv file, it displays the recent balance.                                                                                                                                                                                                                                                                                                                                                             |
| Transaction table            | Unit testing       | 1. Choose transaction table in menu (4).                                                                                                                                                                                                           | By readin the user's own atm csv file, it displays the table without index in markdown style.                                                                                                                                                                                                                                                                                                                                       |
| Chart                        | Unit testing       | 1. Choose chart in menu (5). 2. Choose deposit, withdrawal or balance and enter the option in number. (1 or 2 or 3).                                                                                                                               | If the number that the user entered is an integer and either 1, 2, or 3, it successfully moves to draw the chart. If the number is not fill the requirement above, the program ask the user to enter number again. Depending on the category the user choose, draws line graph which x_axis is date and y_axis is amount.                                                                                                           |
| Logout                       | Unit testing       | 1. Choose logout in menu (6). 2. Enter y or Y if the user wants to logout,  and enter n or N if the user wants to go back to the main menu.                                                                                                        | If the user doesn't enter y, Y, n, or N, the program asks user to enter the letter again. If the user enters y or Y, it displays "You logged out", exit the program by exit code(1).  If the user enter n or N, it displays the main menu.                                                                                                                                                                                          |
| Going back to Main Menu      | Integrated testing | 1. Enter the number depending on the menu the user chooses. (1 or 2 or 3 or 4 or 5 or 6) 2. Session successfully occurs. 3. Go back to the menu and the user enter the number depending on the menu the user chooses. (1 or 2 or 3 or 4 or 5 or 6) | If the thing that the user entered is an integer and either one of the numbers in menu, program move on to the session depending on the number the user chooses. After the session is done, set option_book as False go back to the code of the main menu, and displays the menu. If the user enter the option number correctly as following the above process, this code runs permanently  except when the user chooses to logout. |
| Overall review               | System testing     | 1. Open the pycharm and start the program. 2. Choose signup or login and follow the procedure above. 3. Choose one of the options from the main menu, go to that session, and follow the procedure above. 4. Choose logout. (y or Y)               | All of the output went through well, and there was no error or confusion during the program. If the user chooses to logout, the program ends successfully without any errors.                                                                                                                                                                                                                                                       |

# Criteria C: Development

## Signup System (Success Criteria 3)
My client requires a system to protect the private data. I thought about using a singup system to accomplish this requrement using if condition, for loop, while loop and the open command to work with csv file.

As you can see in the flow diagram in **Fig3**, if the client choose a signup option in the home option (home_option==1), I defined function called try_singup, this function has three inputs of type string, and the output is a boolean representing True if the user signups correctly or False otherwise.
This is saved in the signup_success.
```.py
if home_option == 1: # Sign up
    def try_signup(signup_username:str, signup_password:str, conf_password:str)->bool:
        signup_success=False
```

Then in line 4, I opened the users.csv file with reading mode, and set data as f.readlines().
From line 7 to 12, I set a loop to read all lines in user.csv file to ask users to enter new username again if the username they set first has already used by other users.
In line 8 and 9, I split each line of username as uname and password as upass.
From line 10 to 12, I set while loop which functions if username singup_username input is in username in user.csv file.
If signup_username is in uname, print error message, and ask users to input their new username in line 12.
```.py
with open('users.csv', mode='r') as f:
            data = f.readlines()

        for line in data:
            uname = line.split(',')[0]
            upass = line.split(',')[1].strip()  # strip() remove \n
            while signup_username in uname:
                print("Your username is invalid")
                signup_username = input("Please enter your new username: ")

```

From line 14 to 18, I set while loop to show error if the password they enter first is different from the confirmation password.
In line 15, if signup_password is different from conf_pasword, I print error message, and I ask to enter new password in line 16.
If sinup_password is the same with conf_password, I break the while loop.
In line 20,if user correctly singup by using username and pass word, I make singup_success True.
```.py
while signup_password != conf_password:
            print("The password dosen't match, please enter the password again: ")
            conf_password = input("[Error] Enter your password again: ")
            if signup_password==conf_password:
                break

        signup_success = True
```

In line 22, if singup_success is True, I set variable line_signup, which username and password they set will be record in line splitting by comma in line23.
Then in line 24, I opened the users.csv file as adding mode, and record line_singup.
Then from line 27 to36, I'll make a default user csv file for each user to record their transaction.
In line 27, I set the first row of atm file to define the colum of the file, "Date", "Description", "Category", "Amount", "Balance".
In line 28, I import datetime, and set variable date as today's date.
In line 29, I set variable description as "-----".
In line 30, I set variable category as "-----".
In line 31, I set variable amount as 0 because there is no transaction happened.
In line 32, I set variable balance as 0 because there is no transaction happened yet.
In line 33, I set variable line_atm_2, which combines five variables that I set above as one line, splitting by comma.

In line 34, I open new csv file which use singup_username for the name of the file, and as writing mode.
In line 35, I connect all values in line_atm_1 by comma, and record each value as colum of atm csv file.
In line 36, I record line_atm_2.
```.py
if signup_success == True:
            line_signup = f"{signup_username},{signup_password}\n"
            with open('users.csv', mode='a') as f:
                data = f.writelines(line_signup)

            line_atm_1 = ["Date", "Description", "Category", "Amount", "Balance"]
            date = datetime.date.today()  # today's date
            description = "-----"
            category = "-----"
            amount = 0
            balance = 0
            line_atm_2 = f"{date},{description},{category},{amount},{balance}\n"
            with open(f'atm{signup_username}.csv', mode='w') as f:
                f.writelines(','.join(line_atm_1) + '\n')
                f.writelines(line_atm_2)
```

If all of these signup process done by successfully, it shows the message in red color in line 38.
In line 40, return singup_success as True, if the user can signup successfully, and end try_signup function.
In line 42 to 44, I ask user to enter username, password, and confirmation password, and put those three inputs in the variable of signup and start try_signup function in line 45.
In line 46, set username variable as username which used in signup to use that username in other sessions.
After signup session ends, it moves to the home questions which asks user to choose signup or login.
```.py
 print( f"{red}You are successfully sign upped!{c_end}")

        return(signup_success)

    in_signup_username = input("Enter your username: ")
    in_signup_password = input("Enter your password: ")
    in_conf_password = input("[Confirmation]Enter your password again: ")
    signup=try_signup(signup_username=in_signup_username,signup_password=in_signup_password,conf_password=in_conf_password)
    username = in_signup_username
    # print(signup)

    print(f"1:Sign up\n2:Login")
    username = ''
    home_option = validate_int(msg="Please choose one, and enter the number: ", menu='', type='option')
    while not home_option in [1, 2]:
        home_option = validate_int(msg="[Error] Please choose one, and enter the number: ", menu='', type='option')
```

## Login System  (Success Criteria 3)
My client requires a system to protect her private data, so I set sign up function as I mentioned above. Since, we have a signup function, I thought creating login system to utilize that username and password effectively to secure a client's account by using if condition, for loop, while loop, and opne command csv file.

As you can see in the flow diagram **Fig4**, if the client choose a login option in the home option (home_option==2), I defined function called try_login, this function has two inputs of type string, and the output is a boolean representing True if the user logins correctly or False otherwise.
This is saved in Login.
```.py
if home_option==2: #Login
    def try_login(name:str, password:str)->bool:
        with open('users.csv', mode='r') as f:
            data = f.readlines()

        Login = False
```

Then in line 3, I opened users.csv file as reading mode, and set vriable data as readlines().
In line 6, I set Login as False.
From line 7 to 12, read the users.csv file by splitting each line by comma, and set the first value as variable uname and the second value as variable upass.
If uname is as same as username and upass is as same as password the user entered, Login becomes True and break loop of reading users.csv file.
In line 13, return Login.
```.py
Login = False
        for line in data:
            uname = line.split(',')[0]
            upass = line.split(',')[1].strip() #strip() remove \n
            if uname == name and upass==password:
                Login=True
                break
        return(Login)
```

From line 16, I create a system to ask user to login and if the user enter wrong password three times, the system won't accept any more login.
I asked to enter username and password in line 17 and 18, and start try_login function by using username and password that the user just entered.
If the password that the user enter is wrong and the number of time they make mistakes was less than three times, I ask the user to enter username and password again, and return result. Also, subtract -1 from attempts.
From line 26 to 28, if the result of login ends as False, which means that the user enter wrong username or password three times, the program exit to secure users' accounts.
```.py
###testing
    attempts = 3
    in_name=input("Enter your username: ")
    in_pass=input("Enter your password: ")
    result= try_login(name=in_name, password=in_pass)
    while result== False and attempts > 1:
        in_name = input("[Error try again] Enter your username: ")
        in_pass = input("[Error try again] Enter your password: ")
        result = try_login(name=in_name, password=in_pass)
        attempts -=1

    if result == False:
        print("Sayonara")
        exit(1) #1 is the code for exit without error
```

In line 30, I set variable username as in_name, which is username that the user enter to login.
```.py
    username = in_name
```

## Cryptocurrency description (Success Criteria 2)
My client requires a description of the cryptocurrency she buy and sell. I thought about researching on the Internet about LTC, and show the description nicely by using, textwrap library tp adjust the length of the sentences in the screen.

In line 1, I set variable description_LTC, and put the description of crypto currency the client uses which is refering the information on the interenet.
In line 2, I set variable description_LTC2, and put "citation" with green color.
In line 3, I set variable description_LTC3, and put first citation.
In line 4, I set variabel description_LTC4, and put second citation.
From line 5 to 8, I set variable, description_LTC_wrap_list, description_LTC_wrap_list3, and description_LTC_wrap_list4 which cut letters if the letter in one line hits length of 100.
From line 9 to 12, I diplay description_LTC_wrap_list, description_LTC2, description_LTC_wrap_list3, and description_LTC_wrap_list4, by connecting cut letters with newline (\n).

```.py
description_LTC=("Litecoing is the second-oldest cryptoncurrency created "
                 "from a fork in the Bitoboin blockchain in 2011 by former "
                 "Google engineer Charlie Lee. Litecoin was released with "
                 "150 pre-mined coins and has a total supply of 84 million coins, "
                 "and its blockchain generates a new block every 2.5 minutes. "
                 "A new hashing algorithm allows to reduce over time to preserce "
                 "the coin's value and faster transaction speeds.\n")
description_LTC2=(f"{green}***Citation***{c_end}")
description_LTC3=("“Litecoin (LTC): What It Is, How It Works, vs. Bitcoin.” Investopedia, 2023,"
                 " www.investopedia.com/articles/investing/040515/what-litecoin-and-how-does-it-work.asp."
                 " Accessed 12 Sept. 2023. Napoletano, E.\n")
description_LTC4=("“What Is Litecoin? How Does It Work?” Forbes, 30 Jan. 2023, www.forbes.com/"
                 "advisor/investing/"
                 "cryptocurrency/litecoin/. Accessed 12 Sept. 2023.")
description_LTC_wrap_list = textwrap.wrap(description_LTC, 100)
description_LTC_wrap_list3=textwrap.wrap(description_LTC3,100)
description_LTC_wrap_list4=textwrap.wrap(description_LTC4,100)
print('\n'.join(description_LTC_wrap_list)+"\n")
print(description_LTC2+"\n")
print('\n'.join(description_LTC_wrap_list3)+"\n")
print('\n'.join(description_LTC_wrap_list4)+"\n")
```

## Deposit System  (Success Criteria 4)
My client requires a system to record deposit of cryptocurrency transaction easily. I thought about using a deposit system to accomplish this, using a csv file.
As you can see the flow diagram from **Fig5**, if the user choose the option deposit after she login (menu_option==1)
In line 2, I set variable date, to define today's date by using imported datetime.
In line 3, I ask user to enter the description of deposit to record the purpose of deposit.
In line 4, I set variable category, as deposit.
In line 5, I ask user to enter the amount of currency that the user wants to deposit and validate the value the user entered is whether integer or not, by using validate_int function.
In line 6, I call balance_calc function from my_lib.py to calculate the balance.
In line 8, I set variable line to combine all five variables above.
In line 9 and 10, I open atm csv file which the file name is unique to depending on users, and open it as adding mode, and record the line variable.
In line 12, after 1 second pause, display "Saved" to inform the user that deposit is recorded.
In line 14, I print the balance by using balance variable to inform the user her current balance.


```.py
if menu_option == 1:  # Deposit
    date = datetime.date.today()  # today's date
    description = input("Please enter the description: ")
    category = "deposit"
    amount = validate_int(msg="Please enter amount to deposit: ", menu="", type="amount")
    balance = balance_calc(df=pd.read_csv(f'atm{username}.csv'), amount=amount)
    
    line = f"{date},{description},{category},{amount},{balance}\n"
    with open(f'atm{username}.csv', mode='a') as f:
        f.writelines(line)
    time.sleep(1)
    print("Saved")
    time.sleep(1)
    print(f"Your balance is {balance}")
        time.sleep(1)
```

## Withdrawal System (Success Criteria 4)
My client requires a system to record withdrawal of cryptocurrency transaction easily. I thought about using a withdrawal system to accomplish this, using if condition and open command csv file.

If the user choose the option withdrawal after she login (menu_option==2).
In line 2, I set variable date, to define today's date by using imported datetime.
In line 3, I ask user to enter the description of withdrawal to record the purpose of deposit.
In line 4, I set variable category, as deposit.
In line 5, I ask user to enter the amount of currency that the user wants to deposit and validate the value the user entered is whether integer or not, by using validate_int function.
In line 6, I call balance_calc function from my_lib.py to calculate the balance.
In line 8, I set variable line to combine all five variables above.
In line 9 and 10, I open atm csv file which the file name is unique to depending on users, and open it as adding mode, and record the line variable.
In line 12, after 1 second pause, display "Saved" to inform the user that withdrawal is recorded.
In line 14, I print the balance by using balance variable to inform the user her current balance.

```.py
    if menu_option == 2:  # Withdrawal
        date = datetime.date.today()  # today's date
        description = input("Please enter the description: ")
        category="withdrawal"
        amount = validate_int(msg="Please enter amount to withdrawal: ", menu="", type="amount")
        amount = -1 * amount
        balance = balance_calc(df=pd.read_csv(f'atm{username}.csv'), amount=amount)
        
        line = f"{date},{description},{category},{amount},{balance}\n"
        with open(f'atm{username}.csv', mode='a') as f:
            f.writelines(line)
        time.sleep(1)
        print("Saved")
        time.sleep(1)
        print(f"Your balance is {balance}")
        time.sleep(1)
```

## Debt classification System (Success Criteria 6)
My client requires a system to know her balance is whether in black or not after she deposits or withdrawals money. I thought creating debt classification system by using balance variable and if condition which are suitable to accomplish this requirement.

I use the variable balance and display "You're not debt", and if the balance is below 0, display "You're debt".
```.py
if balance >= 0:
    print("You're not debt")
else:
    print("You're debt")
```

## Exchange currency System (Success Criteria 5)
My client requires exchange currency system to know how much value she has as a cryptocurrency in a real money value. I thought about using exchange currency system by using function with is getting LTC price data in dollar and yen via url api and if condition.

I called the function get_ltc_price_usd that gets the rate of LTC coin by using CoinGecko api in dollar.
As I refer the documentation of CoinGecko, I called the url to get the price of cryptocurrency, and set litecoin in us dollars in params in line 3 to 7.
Then, if I get the data successfully from the server (response.status_code == 200), I transfer Jason data to python structure data in line 11.
I extract the key of litecoin and usd from the data, and set it in variable ltc_price, and return the price after the function ends in line 12 and 13.
If I fail to get the data from the server, I print error message and ends function with return None in line 14 to 16.
```.py
# get LTC data in dollar
def get_ltc_price_usd():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "litecoin",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        ltc_price = data["litecoin"]["usd"]
        return ltc_price
    else:
        print("Failed to fetch data.")
        return None

ltc_price_usd = get_ltc_price_usd()
```

You can see the same structure for getting LTC price in Japanese yen in line 21 to 36.
```.py
# get LTC data in yen
def get_ltc_price_jpy():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "litecoin",
        "vs_currencies": "jpy"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        ltc_price = data["litecoin"]["jpy"]
        return ltc_price
    else:
        print("Failed to fetch data.")
        return None
ltc_price_jpy = get_ltc_price_jpy()
```

**citation**
“Crypto API Documentation | CoinGecko.” CoinGecko, CoinGecko, 2023, www.coingecko.com/ja/api/documentation. Accessed 3 Oct. 2023.

‌
The functions above was stored in my_lib.py to make my main paython code concise, therefore I called the functions to my main python code, wallet.py, in line 39.
After the user done with deposit or withdrawal, ask the user to choose in which currency unit they want to see their LTC value in line 44, and set the option number as variable currency_exchange and call validate_int function to check it is valid number.
If user enter the number except 1, 2, and 3, the user will be asked again to enter the option number in line 44 and 45.
If the user choose us dollar (currency_exchange == 1), multiply balance and the LtC value in us dollar I get, and print that value in line 46 and 47.
I do the same process for Japanese yen which we can see it in line 48 and 49.
If the user choose option 3, set option_bool as False and exist deposit option on line 50 and 51.
```.py
ltc_price_usd = get_ltc_price_usd()
ltc_price_jpy = get_ltc_price_jpy()
# import exchange currency function from my_lib.py
from  my_lib import get_ltc_price_usd, get_ltc_price_jpy

# after deposit or withdrawal finish successfully
print("Check currency in exchange of\n1: USD\n2: JPY")
currency_exchange = validate_int(msg="Choose the exchange currency: ", menu="", type="currency exchange")
while currency_exchange not in [1,2,3]:
           input(("[Invalid] Please enter currency exchange again:\n1: USD\n2: JPY\n3: skip this"))
       if currency_exchange == 1:
           exchanged_value = f"$ {balance * ltc_price_usd}"
           print(exchanged_value)
       elif currency_exchange == 2:
           exchanged_value = f"¥ {balance * ltc_price_jpy}"
           print(exchanged_value)
       elif currency_exchange ==3:
           option_bool=False
```

Full code of exchange currency system
```.py
```my_lib.py```
# get LTC data in dollar
def get_ltc_price_usd():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "litecoin",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        ltc_price = data["litecoin"]["usd"]
        return ltc_price
    else:
        print("Failed to fetch data.")
        return None

ltc_price_usd = get_ltc_price_usd()

# get LTC data in yen
def get_ltc_price_jpy():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "litecoin",
        "vs_currencies": "jpy"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        ltc_price = data["litecoin"]["jpy"]
        return ltc_price
    else:
        print("Failed to fetch data.")
        return None
ltc_price_jpy = get_ltc_price_jpy()

```wallet.py```
ltc_price_usd = get_ltc_price_usd()
ltc_price_jpy = get_ltc_price_jpy()
# import exchange currency function from my_lib.py
from  my_lib import get_ltc_price_usd, get_ltc_price_jpy

# after deposit or withdrawal finish successfully
print("Check currency in exchange of\n1: USD\n2: JPY")
currency_exchange = validate_int(msg="Choose the exchange currency: ", menu="", type="currency exchange")
while currency_exchange not in [1,2,3]:
           input(("[Invalid] Please enter currency exchange again:\n1: USD\n2: JPY\n3: skip this"))
       if currency_exchange == 1:
           exchanged_value = f"$ {balance * ltc_price_usd}"
           print(exchanged_value)
       elif currency_exchange == 2:
           exchanged_value = f"¥ {balance * ltc_price_jpy}"
           print(exchanged_value)
       elif currency_exchange ==3:
           option_bool=False
```

## Balance System (Success Criteria 6)
My client requires the system to know the balance of her account. I thought creating balance calculation function by using open command csv file to calculate the balance.

Import pandas as pd to read to call csv file in line 1.
Then I opened the function balance_calc, which receive the inputs dataframe and integer in line 2.
If we call the balance_calc function, we extract the value at the last row and last colum of the table from input, and adding amount to calculate the balance in line 3 to 5.
Then the function returns balance.
In main python code, wallet.py, I import balance_calc function from my_lib.py in line 8.
If user choose the menu of balance  (menu_option == 3), the program start the session of balance in line 10.
In line 11, I set variable balance and call the function of balance calc and use user's atm csv file and amount is 0 as are inputs.
In line 12, I set variable today, by using datetime, and insert today's date in that.
In line 13, I set variable msg which shows balance by using variable today and balance.
In line 14, I print balance by using banner_maker function imported from my_lib.py with inputs of msg=msg, space=50, symbol='$'.


```.py
```my_lib.py```
import pandas as pd
def balance_calc(df:pd.core.frame.DataFrame,amount:int):
    last_row = df.iloc[-1]
    balance_pre = last_row.iloc[-1]
    balance = balance_pre + amount
    return balance

```wallet.py```
from  my_lib import balance_calc

if menu_option == 3:  # calculate balance
    balance = balance_calc(df=pd.read_csv(f'atm{username}.csv'), amount=0)
    print(balance)
    today = datetime.date.today()
    msg = f"Your balance {today} is ¥{balance}"
    print(banner_maker(msg=msg, space=50, symbol='$'))
```

## Transaction table System (Success Criteria 4)
My client requires to record and show her deposit and withdrawal data with clear visual. I thought creating transaction table shown in markdown style by using open command atm csv file which records user's deposit and withdrawal data.

If user choose menu of transaction table (menu_option == 4), the program start the session of transaction table, in line 1.
I call user's atm csv file in line 2 by removing the second row of the table which is the default input, and print the data in the csv file in markdown style without index in line 3.
```.py
if menu_option ==4: #Transaction table
    df = pd.read_csv(f'atm{username}.csv', skiprows=[1])
    print(df.to_markdown(index=False))
```

## Chart System (Success Criteria 7)
My client requires a system to see her transaction history visually easy to understandable. I thought creating line graph to show user's deposit, withdrawal, and balance history by using open command user's atm csv file and matplotlib.pyplot library.

In line 1, I imported matplotlib.pyplot as plt to import library to draw graph.
In line 2, I imported pandas library as pd to read csv file.
If user choose menu of transaction table (menu_option == 5), the program start the session of chart, in line 3.
I open user's atm csv file with pandas' function in line 4.
Then, show option of drawing chart, deposit, withdrawal, and balance, and ask user to enter the option number and validate that number by validate_int function in line 5.
```.py
import matplotlib.pyplot as plt
import pandas as pd
if menu_option ==5:
    df = pd.read_csv(f'atm{username}.csv')
    category_choice=validate_int(msg="1: Deposit\n2: Withdrawal\n3: Balance\nChoose the category that you want to see graph: ",menu='',type="category")
    while category_choice not in [1,2,3]:
        category_choice = validate_int(msg="[Invalid] Please enter category again\n1: Deposit\n2: Withdrawal\n3: Balance: ", menu="", type="category")
```

If user choose deposit (category_choice == 1), create new dataframe, dfr, by extracting lines if "Category" colum is "deposit" from the user's atm csv file in line 11.
I set variable x_axis value as "Date" in dfr, and variable y_axis as "Amount" in dfr in line 8 and 9.
I set plot title, legend, x label, y label, and set y axis range as 0 to max value of deposit in line 12 to 16.
In line 17, I plot line graph by using x_axis and y_axis variables.
I rotate the xticks 30 degrees clockwise in line 18.
I display the plot in line 19.
```.py
if category_choice==1:#deposit
        dfr = df[df["Category"] == "deposit"]
        x_axis = dfr.Date
        y_axis = dfr.Amount
        plt.ylim(0, max(y_axis))
        plt.title("Deposit History")
        plt.legend("Deposit")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.ylim(0, max(y_axis))
        plt.plot(x_axis, y_axis)
        plt.xticks(rotation=30)
        plt.show()
```

If user choose withdrawal (category_choice==2) from line 22 to 33, or balance (category_choice==3) from line 34 to 43, follow the same process above.
```.py
elif category_choice==2: #withdrawal
        dfr = df[df["Category"] == "withdrawal"]
        x_axis = dfr.Date
        y_axis = dfr.Amount
        plt.ylim(0, max(y_axis))
        plt.title("Withdrawal History")
        plt.legend("Withdrawal")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.plot(x_axis, y_axis)
        plt.xticks(rotation=30)
        plt.show()
 elif category_choice==3:#Balance
        dfr = df["Balance"]
        x_axis = dfr.Date
        y_axis = dfr.Amount
        plt.title("Balance History")
        plt.legend("Balance")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.plot(x_axis, y_axis)
        plt.xticks(rotation=30)
        plt.show()
```

## Logout System  (Success Criteria 3)
My client requires to log out from her bank ledger to protect her account. I thought creating logout system which ends the program without error by using if condition and exit code to accomplish client's requirements.

If user choose logout (menu_option == 6), I ask user that you want to log out and answer in yYnN in line 1 and 2.
If the letter user entered is not yYnN, I ask again user to enter one of yYnN in line 3.
If the user's choice was yes to log out, I exit from the program without any errors by exit(1) in line 8 to 11.
If the user's choice was no to log out, I set option_bool as False and display the menu again in line 10 to 12.
```.py
if menu_option == 6:
    logout_choice = input("Do you want to log out? (Y/N)")
    while not logout_choice in "yYnN":
        logout_choice = input("[Error] Do you want to log out? (Y/N)")

        if logout_choice in "yY":
            time.sleep(1)
            print('You logged out')
            exit(1)
        else:
            time.sleep(2)
            option_bool = False
```
## Video of my project
https://youtu.be/muYBfP_1LRE


## Citations
1. Napoletano, E. “What Is Litecoin? How Does It Work?” Forbes, 30 Jan. 2023, www.forbes.com/advisor/investing/cryptocurrency/litecoin/. Accessed 12 Sept. 2023.
2. “Litecoin (LTC): What It Is, How It Works, vs. Bitcoin.” Investopedia, 2023, www.investopedia.com/articles/investing/040515/what-litecoin-and-how-does-it-work.asp. Accessed 12 Sept. 2023.
3. upGrad. “Top 12 Commerce Project Topics & Ideas in 2023 [for Freshers].” UpGrad Blog, upGrad Education, 28 Sept. 2022, www.upgrad.com/blog/reasons-why-python-popular-with-developers/. Accessed 4 Oct. 2023.
4. ‌“Is Python Good for Software Development? - BairesDev Blog: Insights on Software Development & Tech Talent.” BairesDev Blog: Insights on Software Development & Tech Talent, 22 June 2022, www.bairesdev.com/blog/is-python-good-for-software-development/. Accessed 4 Oct. 2023.
5. alexandre. “PyCharm: All about the Most Popular Python IDE.” Data Science Courses | DataScientest, 20 Feb. 2023, datascientest.com/en/pycharm-all-about-the-most-popular-python-ide#:~:text=The%20main%20advantages%20of%20PyCharm,error%20highlighting%20improves%20the%20process. Accessed 4 Oct. 2023.
6. Simpson, Scott. “Why Use a Database? - Programming Foundations: Databases.” LinkedIn, 28 Mar. 2019, www.linkedin.com/learning/programming-foundations-databases-2/why-use-a-database#:~:text=%2D%20Databases%20let%20us%20work%20with,they%20help%20us%20avoid%20redundancy. Accessed 4 Oct. 2023.
7. “Crypto API Documentation | CoinGecko.” CoinGecko, CoinGecko, 2023, www.coingecko.com/ja/api/documentation. Accessed 3 Oct. 2023.
