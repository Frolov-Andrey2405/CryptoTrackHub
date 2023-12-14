import os
import threading

import pywebio
import pywebio.input as inp
from pywebio.output import *

from handlers.menu import TaskHandler
from handlers.parser import check_coins_balance


@pywebio.config(theme="dark")
async def main():
    """
    The main function is the entry point of the program.
    It starts a thread to check coins balance and then it calls TaskHandler class to add or list tasks.
    """
    clear()
    threading.Thread(target=check_coins_balance).start()

    task = TaskHandler()
    logo_path = os.path.join("data", "logo.jpg")
    put_image(open(logo_path, "rb").read())

    method = await inp.select(
        "Select the desired option",
        [
            "Add a task",
            "Task list"
        ])

    if "Add a task" == method:
        await task.add_task_in_list()
    elif "Task list" == method:
        task.get_task_list()


if __name__ == "__main__":
    pywebio.start_server(main, host="0.0.0.0", port=4444)

