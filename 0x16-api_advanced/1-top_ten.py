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
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200: 
        response_data = req.json()
        if "data" in response_data:
            for get_data in response_data["data"].get("children", []):
                dat = get_data.get("data")
                title = dat.get("title")
                print(title)
        else:
            print("No data found for the subreddit.")
    else:
        print("Error:", req.status_code)
