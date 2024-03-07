#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    req = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    print(req.text)  # Print response text for debugging

    if req.status_code == 200:
        try:
            data = req.json()["data"]["children"]
            for post in data:
                print(post["data"]["title"])
        except KeyError:
            print("Subreddit does not exist or has no posts.")
    else:
        print("Failed to retrieve data from Reddit API.")
