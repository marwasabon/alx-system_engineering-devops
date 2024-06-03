#!/usr/bin/python3
"""Python script to returns information
about his/her TODO list progress convert the data
to a CSV
"""

if __name__ == "__main__":
    import requests
    import sys
    import csv

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
        with open("{usrId}.csv".format(usrId=usrId), "w+") as f:
            fields = ("id", "username", "status", "title")
            writer = csv.DictWriter(
                    f,
                    fieldnames=fields,
                    lineterminator='\n',
                    quotechar='"',
                    quoting=csv.QUOTE_ALL
                    )
            for task in tasks:
                writer.writerow(dict(
                    id=task['userId'],
                    username=user_req["username"],
                    status=task["completed"],
                    title=task["title"]
                ))
