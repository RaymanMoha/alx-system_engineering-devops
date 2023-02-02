#!/usr/bin/python3
"number of subscribers"

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    json_req = req.json()
    if req.status_code != 200:
        return 0
    return(json_req["data"]["subscribers"])
