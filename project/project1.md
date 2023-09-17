# Crypto Wallet

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

An example of the data stored is 

| Date | Description | Category | Amount  |
|------|-------------|----------|---------|
| Sep 23 2022 | bought a house | Expenses | 10 BTC |
| Sep 24 2022 | food for house celebration | Food | 0.000001 BTC |


## Proposed Solution

Design statement:
I will to design and make a electronic ledger for a client who is Ms.Sato. The electronic ledger will about the system which records transaction of cryptocurrency and is constructed using the software PyCharm. It will take 1 month to make and will be evaluated according to the criteria below.

** add a description of your coin and citation **
Litecoing is the second-oldest cryptoncurrency created from a fork in the Bitoboin blockchain in 2011 by former Google engineer Charlie Lee. Litecoin was released with 150 pre-mined coins and has a total supply of 84 million coins, and its blockchain generates a new block every 2.5 minutes. A new hashing algorithm allows to reduce over time to preserce the coin's value and faster transaction speeds.

“Litecoin (LTC): What It Is, How It Works, vs. Bitcoin.” Investopedia, 2023, www.investopedia.com/articles/investing/040515/what-litecoin-and-how-does-it-work.asp. Accessed 12 Sept. 2023.
Napoletano, E. “What Is Litecoin? How Does It Work?” Forbes, 30 Jan. 2023, www.forbes.com/advisor/investing/cryptocurrency/litecoin/. Accessed 12 Sept. 2023.

‌
Justify the tools/structure of your solution

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger display the exchange of currency (yen and dollars).
5. The electronic ledger has sign up, log in, and log out system.
6. The electronic ledger display the menu of function, enter, withdraw, transaction table, graph, log out.
7. The electronic ledger display profit after user enter or withdraw cryptocurrency.
8. The electronic ledger shows the past transaction table.
9. The electronic ledger display the bar chart of transaction and profit.
10. The electronic ledger display the pie chart depending on the category of expense.

# Criteria B: Design

## System Diagram
![Computer Science quiz](https://github.com/Happa1/unit1-2024/assets/142579414/9263bde9-216f-4903-a4c3-f2d900617763)
**Fig. 3** This is the System Diagram of the project with starts from input by keyboard, and ends with output by screen done 

## Flow Diagrams
![IMG_9024 Large](https://github.com/Happa1/unit1-2024/assets/142579414/75ca2911-61da-4ece-8a17-c0245a37eb84)

**Fig. 2** This is the flow diagram for the login system.

## Record of Tasks
| Task No | Planned Action        | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |
|---------|-----------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram | To have a clear idea of the hardware and software requirements for the proposed solution | 15min         | Sep 13                 | B         |
| 2       | Create a login System | To have a flow diagram and the code for the login system                                 | 30min         | Sep14                  | B, C      |
|         |                       |                                                                                          |               |                        |           |

# Criteria C: Development

## Login System
My client requires a system to protect the private data. I thought about using a login system to accomplish this requirement using a if condition and the open command to work with a csv file. More description of the code....

As you can see in the flow diagram in **Fig 1**, In the first line I am defininf a function called try_login, this function has two inputs of type string, and the output is a boolean representing True if the user logins correctly or false otherwise. This is saved in the variable success. Then in line two...this is your work.
```.py
def try_login(name:str, password:str)->bool:
    with open('users.scv',mode='r') as f:
        data = f.readlines()

    success = False
    for line in data:
        uname = line.split(',')[0]
        upass = line.split(',')[1].strip() #strip() remove \n
        if uname == name and upass==password:
            success=True
            break
    return(success)

###testing
attempts = 3
in_name=input("Enter your username")
in_pass=input("Enter your password")
result= try_login(name=in_name, password=in_pass)
while result== False and attempts > 1:
    in_name = input("[Error try again] Enter your username")
    in_pass = input("[Error try again] Enter your password")
    result = try_login(name=in_name, password=in_pass)
    attempts -=1

if result == False:
    print("Sayonara")
    exit(1) #1 is the code for exit without error

#The program continue here if it does close
print("Welcome")
#the test of your program

```

