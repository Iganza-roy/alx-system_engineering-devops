#!/usr/bin/python3
"""querrying the reddit API"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Edge/125.0.2535.79"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(top.get("data").get("title")) for top in results.get("children")]
