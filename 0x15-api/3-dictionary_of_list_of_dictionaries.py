#!/usr/bin/python3

"""A Python script that, using this REST API, for a given employee ID."""

import json
import requests
from sys import argv


def display_tasks():
    """Export data in the specified format."""

    link = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(link + "/users")
    user_data = user_response.json()

    tasks_response = requests.get(link + "/todos")
    tasks_data = tasks_response.json()

    output_data = {}

    for user in user_data:
        user_id = user.get("id")

        user_tasks = []
        for task in tasks_data:
            if task.get("userId") == user_id:
                task_info = {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                user_tasks.append(task_info)

        output_data.update({str(user_id): user_tasks})

    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(output_data, json_file)


if __name__ == "__main__":
    display_tasks()
