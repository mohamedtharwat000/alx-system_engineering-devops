#!/usr/bin/python3

"""Script that, using REST API, for a given employee ID."""

import requests
import sys

ID = sys.argv[1]

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
