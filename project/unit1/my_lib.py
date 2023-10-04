def banner_maker(msg:str, symbol:str, space:int)->str:
    height=5
    width=2+2*space+len(msg)
    end_code="\33[00m"
    green="\033[0;92m"

    top_line=symbol*width
    middle_line=symbol + " "*(width-2) + symbol
    msg_line=symbol + " "*space + msg.upper() + " "*space + symbol

    banner=f"{top_line}\n{middle_line}\n{green}{msg_line}{end_code}\n{middle_line}\n{top_line}"
    return banner

def print_menu(menu):
    for i in range(len(menu)):
        print(f"\033[9{i+1}m{i + 1}.{menu[i]}\033[00m")

def validate_int(msg:str, menu, type):
    option = input(msg)
    while not option.isdigit():
        print(f"\033[91m[Error]\033[00m")
        print_menu(menu)
        option = input(f"Please enter {type} again: ")
    return int(option)

import requests
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
# LTCの価格を取得
ltc_price_usd = get_ltc_price_usd()

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

import pandas as pd
def balance_calc(df:pd.core.frame.DataFrame,amount:int):
    last_row = df.iloc[-1]
    balance_pre = last_row.iloc[-1]
    balance = balance_pre + amount
    return balance
