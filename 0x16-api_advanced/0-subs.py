#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}

    try:
        req = requests.get(url, headers=headers)
        req.raise_for_status()  # Raise an error for unsuccessful status codes
        data = req.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
    except KeyError as e:
        print(f"Error: Key not found in JSON response - {e}")
        return 0
