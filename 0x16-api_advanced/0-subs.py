#!/usr/bin/python3
"""querrying the reddit API"""
import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit"""
    if not subreddit or not isinstance(subreddit, str):
        return 0
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            "User-Agent": "Edge/125.0.2535.79 "
        }
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 404:
            return 0
        results = response.json().get("data")
        return results.get("subscribers")

    except Exception:
        return 0
