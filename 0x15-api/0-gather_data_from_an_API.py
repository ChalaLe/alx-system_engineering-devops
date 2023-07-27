#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

def get_todo_list_info(employee_id):
    """
    Retrieves and prints to-do list information for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_info(employee_id)
