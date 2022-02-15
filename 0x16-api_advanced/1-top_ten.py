#!/usr/bin/python3


'''task 1'''


import requests


def top_ten(subreddit):
    headers = {'User-agent': 'test'}
    responce = requests.get('http://www.reddit.com/r/{}/hot.json'
                            .format(subreddit),
                            headers=headers, params={'limit': '10'})
    if responce.status_code == 200:
        for post in responce.json()['data']['children']:
            print(post['data']['title'])
    else:
        print('None')
