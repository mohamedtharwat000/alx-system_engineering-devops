#!/usr/bin/python3

"""A Python script that, using this REST API, for a given employee ID."""

import requests
from sys import argv


def display_tasks():
    """fetches data for a given employee ID."""

    link = "https://jsonplaceholder.typicode.com/users/"

    response = requests.get(link + argv[1])

    data = response.json()

    name = data.get("name")
    print("Employee {} is done with tasks".format(name), end="")

    response = requests.get(link + argv[1] + "/todos")

    data = response.json()

    tasks = []
    for task in data:
        if task.get("completed") is True:
            tasks.append(task.get("title"))
    print("({}/{}):".format(len(tasks), len(data)))

    for task in tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    display_tasks()
