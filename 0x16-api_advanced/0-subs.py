#!/usr/bin/python3
"""Python scripts that retruns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Function that returns  the number of users subscribed to reddit
    """
    try:
        h = {'user-agent': 'Mozilla/5.0', 'allow_redirects': 'false'}
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        req = requests.get(url, headers=h)
        return req.json().get('data').get('subscribers', 0)
    except Exception as e:
        return 0

def number_of_subscribersi(subreddit):
    """Function that returns  the number of users subscribed to reddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
