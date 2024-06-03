#!/usr/bin/python3
"""Python script to returns information about his/her TODO list progress"""
import json
import requests


if __name__ == "__main__":

    entrypoint = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(entrypoint)).json()
    tasks = requests.get("{}/todos".format(entrypoint)).json()

    collected_tasks = {}

    for usr in users:
        user_id = usr["id"]
        usr_task = []

        user_tasks = [t for t in tasks if t['userId'] == user_id]

        for task in user_tasks:
            user_task = {
                "username": usr["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            usr_task.append(user_task)

        collected_tasks[user_id] = usr_task

    with open("todo_all_employees.json", "w+") as f:
        json.dump(collected_tasks, f, indent=2)
