#!/usr/bin/python3

"""A Python script that, using this REST API, for a given employee ID."""

import json
import requests
from sys import argv

def display_tasks():
    """Export data in the specified format."""

    link = "https://jsonplaceholder.typicode.com/users/"

    user_response = requests.get(link + argv[1])
    user_data = user_response.json()
    user_id = user_data.get("id")
    username = user_data.get("username")

    tasks_response = requests.get(link + argv[1] + "/todos")
    tasks_data = tasks_response.json()

    output_data = {str(user_id): []}
    for task in tasks_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        output_data.get(str(user_id)).append(task_info)

    with open(f"{user_id}.json", mode='w') as json_file:
        json.dump(output_data, json_file)

if __name__ == "__main__":
    display_tasks()
