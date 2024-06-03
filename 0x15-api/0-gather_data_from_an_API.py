#!/usr/bin/python3
"""Python script to returns information about his/her TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    entrypoint = "https://jsonplaceholder.typicode.com"
    usrId = sys.argv[1]
    user_req = requests.get(
            "{ep}/users/{usrId}".format(ep=entrypoint, usrId=usrId)
            ).json()
    if user_req:
        tasks = requests.get(
                "{ep}/todos".format(ep=entrypoint),
                params={"userId": usrId}
                ).json()
        num_of_tasks = len(tasks)
        finished_tasks = [t for t in tasks if t['completed'] is True]
        print(
                "Employee {} is done with tasks({}/{}):"
                .format(user_req['name'], len(finished_tasks), num_of_tasks)
                )
        [print('\t ' + task['title']) for task in finished_tasks]
