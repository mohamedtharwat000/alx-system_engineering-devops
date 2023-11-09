#!/usr/bin/python3

"""queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about"

    if not subreddit:
        return 0

    response = requests.get(url, allow_redirects=False, timeout=10)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
