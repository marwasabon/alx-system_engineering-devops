#!/usr/bin/python3
"""Python scripts that retruns the number of subscribers"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Function that returns  the number of users subscribed to reddit"""
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        req = requests.get(url)
        return req.json().get('data').get('subscribers', 0)
    except Exception as e:
        return 0


if __name__ == "__main__":
    pass
