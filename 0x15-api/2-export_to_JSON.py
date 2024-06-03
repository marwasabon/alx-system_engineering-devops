#!/usr/bin/python3
"""Python script to returns information
about his/her TODO list progress export data in the JSON format.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    entrypoint = "https://jsonplaceholder.typicode.com"
    usrId = sys.argv[1]
    user_req = requests.get(
            "{ep}/users/{usrId}".format(ep=entrypoint, usrId=usrId)
            ).json()
    if user_req:
        tasks = requests.get(
                "{ep}/todos".format(ep=entrypoint),
                params={"id": usrId}
                ).json()
        with open("{}.json".format(usrId), "w+") as f:
            # someway to get the id
            usr_task = {usrId: []}
            for task in tasks:
                t_d = dict(
                        task=task["title"],
                        completed=task["completed"],
                        username=user_req["username"],
                        )
                usr_task[usrId].append(t_d)
                json.dump(usr_task, f)
