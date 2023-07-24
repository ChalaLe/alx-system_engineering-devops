#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_employee_todo_progress(employee_id):
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user = requests.get(url_users).json()
    todos = requests.get(url_todos).json()

    print("Response from API:", todos)  # Add this print statement to inspect the response

    if todos:
        employee_name = user.get("username")  # Check the correct key for the employee's username
        completed_tasks = [task for task in todos if task.get("completed")]
        total_tasks = len(todos)

        print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
        for task in completed_tasks:
            print("\t {}".format(task.get("title")))

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
