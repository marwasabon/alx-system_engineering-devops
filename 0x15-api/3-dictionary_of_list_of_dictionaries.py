#!/usr/bin/python3
"""Python script to returns information about his/her TODO list progress"""
import json
import requests


if __name__ == "__main__":

    entrypoint = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(entrypoint)).json()
    tasks = requests.get("{}/todos".format(entrypoint)).json()

    with open("todo_all_employees.json", "w+") as f:
        collected_tasks = dict()
        for usr in users:
            usr_id = usr["id"]
            usr_task = {usr_id: []}
            user_tasks = [t for t in tasks if t['id'] == usr_id]
            for t in user_tasks:
                task = dict(
                        username=usr["username"],
                        task=t["title"],
                        completed=t["completed"]
                        )
                tasks.remove(t)
                usr_task[usr_id].append(task)
                collected_tasks.update(usr_task)
                json.dump(collected_tasks, f)
