#!/usr/bin/python3

"""A Python script that, using this REST API, for a given employee ID."""

import csv
import requests
from sys import argv


def display_tasks():
    """export data in the CSV format."""

    link = "https://jsonplaceholder.typicode.com/users/"

    user_response = requests.get(link + argv[1])
    user_data = user_response.json()
    user_id = user_data.get("id")
    username = user_data.get("username")

    tasks_response = requests.get(link + argv[1] + "/todos")
    tasks_data = tasks_response.json()

    with open(f"{user_id}.csv", mode='w', newline='') as csv_file:

        fieldnames = [
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for task in tasks_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
            })


if __name__ == "__main__":
    display_tasks()
