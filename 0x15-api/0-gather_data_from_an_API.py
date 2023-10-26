#!/usr/bin/python3

"""Script that returns information about TODO list progress."""

import requests
from sys import argv

def display_tasks():
    """fetches data for a given employee ID."""
    ID = argv[1]

    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{ID}', timeout=10)
    user_data = user_response.json()

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={ID}', timeout=10)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = len([task for task in todos_data if task.get('completed')])


    # Display the progress
    print(
        f"Employee {user_data.get('name')} \
is done with tasks ({completed_tasks}/{total_tasks}):")

    for task in todos_data:
        if task['completed']:
            print(f"\t{task.get('title')}")

if __name__ == "__main__":
    display_tasks()
