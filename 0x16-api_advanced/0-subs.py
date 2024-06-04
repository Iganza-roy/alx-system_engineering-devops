#!/usr/bin/python3
"""querrying the reddit API"""
import requests

def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit"""
    red_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent-v1.0'}
    
    try:
        response = requests.get(red_url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
