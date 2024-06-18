#!/usr/bin/python3
"""Python scripts that retruns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Function that returns  the number of users subscribed to reddit"""
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = requests.get(url, headers, allow_redirects=False)
        return request.json().get('data').get('subscribers',0)
    except Exception as e:
        return 0
