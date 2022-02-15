#!/usr/bin/python3


'''task 0'''


import requests


def numbers_of_subscribers(subreddit):
    headers = {'User-agent': 'test'}
    responce = requests.get(f'http://www.reddit.com/r/{subreddit}/about.json', headers=headers)
    if responce.status_code == 200:
        return responce.json()['data']['subscribers']
    else:
        return 0



if __name__ == "__main__":
    numbers_of_subscribers('programming')