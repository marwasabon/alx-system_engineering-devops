#!/usr/bin/python3
"""Python scripts that retruns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

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
