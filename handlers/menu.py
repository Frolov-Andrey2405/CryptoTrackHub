import asyncio
import json
from functools import partial

import pywebio.input as inp
from pywebio.output import *
from pywebio.session import run_js


class TaskHandler:
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the initial values for all of our variables, and creates a list of coins that we want to track.
        """
        self.__coins = ["BTC", "ETH"]

    @staticmethod
    def read_task_file():
        """
        The read_task_file function reads the task.json file and returns a dictionary containing all of its contents.
        """
        with open("task.json", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def add_task_to_file(data: dict):
        """
        The add_task_to_file function takes a dictionary as an argument.
        It then reads the task file and stores it in a variable called last_changes.
        The function then adds the data from the dictionary to last_changes, which is now a list of dictionaries.
        Then, it writes that list of dictionaries to task.json.
        """
        last_changes = TaskHandler.read_task_file()
        last_changes[data["name"]] = data["price to alert"]
        with open("task.json", "w", encoding="utf-8") as file:
            json.dump(last_changes, file, indent=4)

    @staticmethod
    def delete_task_in_file(coin_name, update=True):
        """
        The delete_task_in_file function deletes a task from the task.json file.
        It takes in two arguments: coin_name and update (defaults to True).
        The coin_name argument is the name of the cryptocurrency that you want to delete from your list of tasks.
        The update argument determines whether or not you want to reload your page after deleting a task.
        """
        last_changes = TaskHandler.read_task_file()
        try:
            del last_changes[coin_name]

            with open("task.json", "w", encoding="utf-8") as file:
                json.dump(last_changes, file, indent=4)
        except KeyError:
            print("The key is missing from the task list")
        if update:
            run_js("location.reload()")

    @staticmethod
    def get_task_list():
        """
        The get_task_list function is used to display the tasks that are currently in the task file.
        It does this by reading the task file and then displaying it as a table with three columns: name, price to alert, and delete?.
        The first column displays all of the names of each item in alphabetical order. The second column displays all of their prices to alert in numerical order from least expensive to most expensive. The third column has a button for each item that allows you to delete them from your list.
        """
        result = []
        task = TaskHandler.read_task_file()

        for name, price in task.items():
            result.append([
                name,
                price,
                put_button(f"delete {name}", onclick=partial(TaskHandler.delete_task_in_file, name))
            ])

        put_table(
            result,
            header=["name", "price to alert", "delete?"]
        )
        put_button("Back", onclick=lambda: run_js("location.reload()"))

    # Валидация форм для отправки
    @staticmethod
    def add_task_validate(data):
        """
        The add_task_validate function is used to validate the data that is entered into the form.
        It checks if there are any empty fields and returns an error message if so.
        """
        if data is None or data == "":
            return "price", "It is necessary to fill in the field"

    async def add_task_in_list(self):
        """
        The add_task_in_list function is used to add a task in the list of tasks.
        It takes two parameters: self and coin_ticker. The first parameter, self, is the instance of TaskHandler class that calls this function.
        The second parameter, coin_ticker, is a string representing the name of the cryptocurrency whose price we want to monitor.
        """
        coin_ticker = await inp.select("Pick a coin", self.__coins, multiple=False)
        price = await inp.input('Enter the expected price', validate=TaskHandler.add_task_validate)

        if all([coin_ticker, price]):
            toast("The task has been successfully created")
            await asyncio.sleep(1)
            run_js("location.reload()")
            TaskHandler.add_task_to_file({
                "name": coin_ticker.lower(),
                "price to alert": price.replace('.', '',).replace(',', '').lower()
            })

