#!/usr/bin/python3


'''task 2'''


import requests


def recursive(subreddit, hot_list=[], next=None):
    headers = {'User-agent': 'test'}
    responce = requests.get('http://www.reddit.com/r/{}/hot.json'
                            .format(subreddit),
                            headers=headers)
    next = responce.json()['data']['after']
    posts = responce.json()['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    if next is not None:
        recursive(subreddit, hot_list, next)
    return hot_list
