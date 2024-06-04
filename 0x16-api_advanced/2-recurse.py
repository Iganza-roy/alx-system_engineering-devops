#!/usr/bin/python3
"""querrying the reddit API."""
import requests


def recurse(subreddit, hot_list=[]):
    """function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Edge/125.0.2535.79"}

    try:
        response = get(url, headers=headers)
        data = response.json()

        if 'error' in data:
            return None

        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']

        if after:
            return recurse(subreddit, hot_list)
        else:
            return hot_list

    except Exception:
        return None
