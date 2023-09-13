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
I will to design and make a ———— for a client who is Ms.Sato. The ——– will about ———— and is constructed using the software PyCharm. It will take  ———- to make and will be evaluated according to the criteria ———.

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
4. The electronic ledger display profit.
5. The electronic ledger shows the past transaction table.
6. The electronic ledger display the graph of transaction and profit.

# Criteria B: Design

## System Diagram
![Computer Science quiz](https://github.com/Happa1/unit1-2024/assets/142579414/9263bde9-216f-4903-a4c3-f2d900617763)
Figure1: This is the System Diagram of the project with starts from input by keyboard, and ends with output which dsplayed

## Flow Diagrams


## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram                                         | To have a clear idea of the hardware and software requirements for the proposed solution                        | 10min         | Sep 24                 | B         |

# Criteria C: Development

## Login System
My client requires a system to protect the private data. I thought about using a login system to accomplish this requirement using a if condition and the open command to work with a csv file. More description of the code....
```.py
def simple_login(user:str, password:str)->bool:
    '''
    Simple authentication, needs fle user.csv
    :param user: string
    :param password: string
    :return: True/False if user is in database
    '''
    with open("user.csv") as file:
        database = file.readlines()
    output = False
    for line in database:
        line_cleaned = line.strip() #remove \n
        user_pass = line_cleaned.split(",")
        if user == user_pass[0] and password == user_pass[1]:
            output = True
            break

    return output


```
