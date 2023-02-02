#!/usr/bin/python3
"top recursive"

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url,
                       headers={'user-agent': 'Mozilla/5.0'},
                       allow_redirects=False,
                       params={'after': after})
    if req.status_code != 200:
        return None
    json_req = req.json()
    for post in json_req["data"]["children"]:
        hot_list.append(post["data"]["title"])
    if json_req["data"]["after"] is not None:
        recurse(subreddit, hot_list, json_req["data"]["after"])
    return hot_list
