#!/usr/bin/python3
"""querrying the reddit API"""
import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.48"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
