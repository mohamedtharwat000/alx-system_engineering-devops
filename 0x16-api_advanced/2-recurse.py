#!/usr/bin/python3

"""queries the Reddit API and returns a list containing the titles\
of all hot articles"""

import requests

def recurse(subreddit, hot_list=None):
    """returns a list containing the titles of all hot articles"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            title = response.json()["data"]["children"][i]["data"]["title"]
            hot_list.append(title)
        return hot_list
    else:
        return None
