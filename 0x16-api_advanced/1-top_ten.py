#!/usr/bin/python3
"""Python scripts that retruns the calls the function below"""
import requests
from sys import argv


def top_ten(subreddit):
    """Function that returns queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit."""
    try:
        hs = {'user-agent': 'Mozilla/5.0', 'allow_redirects': 'false'}
        p = {'limit': 10}
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        req = requests.get(url, headers=hs, params=p).json().get('data')

        for post in req.get('children'):
            print(post.get('data', None).get('title', None))

    except Exception as e:
        print(None)
