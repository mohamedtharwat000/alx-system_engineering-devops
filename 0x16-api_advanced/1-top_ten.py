#!/usr/bin/python3

"""queries the Reddit API and prints the titles of the first 10 posts"""

import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print("None")
