import sys
import time

import requests
from bs4 import BeautifulSoup

from handlers.menu import TaskHandler


def get_crypto_rank(coins):
    """
    The get_crypto_rank function takes a list of coins and returns a dictionary
    with the coin tickers as keys and their prices in USD as values.
    """
    result = {}
    html_resp = requests.get("https://coinranking.com/ru").text
    block = BeautifulSoup(html_resp, "lxml")
    rows = block.find_all("tr", class_="table__row--full-width")

    for row in rows:
        ticker = row.find("span", class_="profile__subtitle-name")
        if ticker:
            ticker = ticker.text.strip().lower()

            if ticker in coins:
                price = row.find("td", class_="table__cell--responsive")
                if price:
                    price = int(float(price.find("div", class_="valuta--light").text\
                                .replace("$", "").replace(",", ".").replace(" ", "")\
                                .replace("\n", "").replace("\xa0", "")))
                result[ticker.lower()] = price
    return result

def check_coins_balance():
    """
    The check_coins_balance function is a loop that checks the current price of each coin in the task file.
    If the current price is less than or equal to the desired price, it sends a notification and deletes that coin from
    the task file.
    """
    while True:
        coins = TaskHandler.read_task_file()
        coin_dict = get_crypto_rank(coins.keys())

        for name, price in coins.items():
            if name in coin_dict:
                if coin_dict[name] <= int(price):
                    TaskHandler.delete_task_in_file(name, update=False)

        time.sleep(20)
