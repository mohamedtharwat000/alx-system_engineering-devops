#!/usr/bin/python3

"""returns a list containing the titles of all hot articles"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """returns a list containing the titles of all hot articles"""

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}

    if after:
        url += f'&after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if not posts:
            return hot_list

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']

        return recurse(subreddit, hot_list, after)
    else:
        return None
