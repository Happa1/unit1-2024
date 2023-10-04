import pandas as pd
import time
import textwrap
import datetime
import matplotlib.pyplot as plt


from  my_lib import banner_maker, print_menu, validate_int, get_ltc_price_usd, get_ltc_price_jpy, balance_calc

red="\033[91m"
green="\033[92m"
yellow="\033[93m"
blue="\033[94m"
purple="\033[95m"
lblue="\033[96m"
white="\033[97m"
c_end="\033[00m"

ltc_price_usd = get_ltc_price_usd()
ltc_price_jpy = get_ltc_price_jpy()


print(f"1: Sign up\n2: Login")
username=''
home_option=validate_int(msg="Please choose one, and enter the number: ", menu='',type='option')
while not home_option in [1,2]:
    home_option=validate_int(msg=f"{red}[Error]{c_end} Please choose one, and enter the number: ", menu='',type='option')

# home_option = int(input("please choose one, and enter the number: "))

if home_option == 1: # Sign up
    def try_signup(signup_username:str, signup_password:str, conf_password:str)->bool:
        signup_success=False
        with open('users.csv', mode='r') as f:
            data = f.readlines()

        for line in data:
            uname = line.split(',')[0]
            upass = line.split(',')[1].strip()  # strip() remove \n
            while signup_username in uname:
                print("Your username is invalid")
                signup_username = input("Please enter your new username: ")

        while signup_password != conf_password:
            print(f"{red}[Error]{c_end} The password dosen't match, please enter the password again: ")
            conf_password = input(f"{red}[Error]{c_end} Enter your password again: ")
            if signup_password==conf_password:
                break

        signup_success = True

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

        print( f"{red}You are successfully sign upped!{c_end}\n")

        return(signup_success)

    in_signup_username = input("Enter your username: ")
    in_signup_password = input("Enter your password: ")
    in_conf_password = input(f"{green}[Confirmation]{c_end} Enter your password again: ")
    signup=try_signup(signup_username=in_signup_username,signup_password=in_signup_password,conf_password=in_conf_password)
    username = in_signup_username
    # print(signup)

    print(f"1:Sign up\n2:Login")
    username = ''
    home_option = validate_int(msg="Please choose one, and enter the number: ", menu='', type='option')
    while not home_option in [1, 2]:
        home_option = validate_int(msg=f"{red}[Error]{c_end} Please choose one, and enter the number: ", menu='', type='option')

if home_option==2: #Login
    def try_login(name:str, password:str)->bool:
        with open('users.csv', mode='r') as f:
            data = f.readlines()

        Login = False
        for line in data:
            uname = line.split(',')[0]
            upass = line.split(',')[1].strip() #strip() remove \n
            if uname == name and upass==password:
                Login=True
                break
        return(Login)

    ###testing
    attempts = 3
    in_name=input("Enter your username: ")
    in_pass=input("Enter your password: ")
    result= try_login(name=in_name, password=in_pass)
    while result== False and attempts > 1:
        in_name = input(f"{red}[Error]{c_end} Enter your username: ")
        in_pass = input(f"{red}[Error]{c_end} Enter your password: ")
        result = try_login(name=in_name, password=in_pass)
        attempts -=1

    if result == False:
        print("Sayonara")
        exit(1) #1 is the code for exit without error

    username = in_name


# menu option
time.sleep(1)

def userinfo():
    return username

msg = banner_maker(msg=f"{username}-san, Welcome to ATM", space=50, symbol="$")
print(msg+"\n")
time.sleep(1)

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
time.sleep(2)

def menu_main():
    while True:
        menu = ["Deposit", "Withdraw", "Balance", "Transaction table", "Chart", "Logout"]
        print("The menu is:")
        print_menu(menu)
        time.sleep(1)
        option = validate_int(msg="Please enter an option: ", menu=menu, type="option")
        # option = 7  # this could be any value but 1, 2, or 3
        while option not in [1, 2, 3, 4, 5, 6]:
            option = validate_int(msg=f"{red}[Invalid option]{c_end} Please enter an option: ", menu=menu, type="option")
        return option

option_bool=False
while option_bool == False:
    menu_option=menu_main()
    option_bool=True

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
        print("Saved\n")
        time.sleep(1)
        print(f"Your balance is {balance}\n")
        time.sleep(1)
        if balance>=0:
            print("You're not debt\n")
        else:
            print("You're debt\n")
        time.sleep(1)
        print("Check currency in exchange of\n1: USD\n2: JPY\n3: skip this")
        currency_exchange=validate_int(msg="Choose the exchange currency: ", menu="", type="currency exchange")
        while currency_exchange not in [1,2,3]:
            currency_exchange = validate_int(msg=f"{red}[Invalid]{c_end} Please enter currency exchange again:\n1: USD\n2: JPY\n3: skip this: ", menu="", type="currency exchange")
        if currency_exchange == 1:
            exchanged_value = f"You currently have $ {balance * ltc_price_usd}\n"
            print(exchanged_value)
        elif currency_exchange == 2:
            exchanged_value = f"You currently have ¥ {balance * ltc_price_jpy}\n"
            print(exchanged_value)
        elif currency_exchange ==3:
            option_bool=False
        time.sleep(2)
        option_bool=False

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
        print("Saved\n")
        time.sleep(1)
        print(f"Your balance is {balance}\n")
        time.sleep(1)
        if balance>=0:
            print("You're not debt\n")
        else:
            print("You're debt\n")
        time.sleep(1)
        print("Check currency in exchange of\n1: USD\n2: JPY\n3: skip this")
        currency_exchange = validate_int(msg="Choose the exchange currency: ", menu="", type="currency exchange")
        while currency_exchange not in [1,2,3]:
            input((f"{red}[Invalid]{c_end} Please enter currency exchange again:\n1: USD\n2: JPY\n3: skip this"))
        if currency_exchange == 1:
            exchanged_value = f"You currently have $ {balance * ltc_price_usd}\n"
            print(exchanged_value)
        elif currency_exchange == 2:
            exchanged_value = f"You currently have ¥ {balance * ltc_price_jpy}\n"
            print(exchanged_value)
        elif currency_exchange ==3:
            option_bool=False
        time.sleep(2)
        option_bool = False

    if menu_option == 3:  # calculate balance
        balance = balance_calc(df=pd.read_csv(f'atm{username}.csv'), amount=0)
        today = datetime.date.today()
        msg = f"Your balance {today} is {balance}"
        print(banner_maker(msg=msg, space=50, symbol='$'))
        time.sleep(2)
        option_bool = False

    if menu_option ==4: #Transaction table
        df = pd.read_csv(f'atm{username}.csv', skiprows=[1])
        print(df.to_markdown(index=False))
        time.sleep(2)
        option_bool = False


    if menu_option ==5:
        df = pd.read_csv(f'atm{username}.csv')
        category_choice=validate_int(msg="1: Deposit\n2: Withdrawal\n3: Balance\nChoose the category that you want to see graph: ",menu='',type="category")
        while category_choice not in [1,2,3]:
            category_choice = validate_int(msg=f"{red}[Invalid]{c_end} Please enter category again\n1: Deposit\n2: Withdrawal\n3: Balance: ", menu="", type="category")
        if category_choice==1:
            dfr = df[df["Category"] == "deposit"]
            x_axis = dfr.Date
            y_axis = dfr.Amount
            plt.ylim(0, max(y_axis))
            plt.title("Deposit History")
            plt.legend("Deposit")
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.plot(x_axis, y_axis)
            plt.xticks(rotation=30)
            plt.show()
            time.sleep(1)
            print("Please check the graph\n")
        elif category_choice==2:
            dfr = df[df["Category"] == "withdrawal"]
            x_axis = dfr.Date
            y_axis = dfr.Amount
            plt.title("Withdrawal History")
            plt.legend("Withdrawal")
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.plot(x_axis, y_axis)
            plt.xticks(rotation=30)
            plt.show()
            time.sleep(1)
            print("Please check the graph\n")
        elif category_choice==3:
            dfr = df["Balance"]
            x_axis = df["Date"]
            y_axis = df["Balance"]
            plt.title("Balance History")
            plt.legend("Balance")
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.plot(x_axis, y_axis)
            plt.xticks(rotation=30)
            plt.show()
            time.sleep(1)
            print("Please check the graph\n")
        time.sleep(2)
        option_bool = False

    if menu_option==6:
        logout_choice=input("Do you want to log out? (Y/N)")
        while not logout_choice in "yYnN":
            logout_choice = input(f"{red}[Error]{c_end} Do you want to log out? (Y/N)")

        if logout_choice in "yY":
            time.sleep(1)
            print('You logged out')
            exit(1)
        else:
            time.sleep(2)
            option_bool = False
