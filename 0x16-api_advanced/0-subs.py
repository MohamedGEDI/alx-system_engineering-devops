#!/usr/bin/python3


'''task 0'''


import requests


def number_of_subscribers(subreddit):
    headers = {'User-agent': 'test'}
    responce = requests.get('http://www.reddit.com/r/{}/about.json'
                            .format(subreddit),
                            headers=headers)
    if responce.status_code == 200:
        return responce.json()['data']['subscribers']
    else:
        return 0
