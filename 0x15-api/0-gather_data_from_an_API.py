#!/usr/bin/python3
''' task 0 module'''


if __name__ == "__main__":
    import requests
    import sys

    param = sys.argv[1]
    total_todos = 0
    done_todos = 0
    todos_title = []
    responce = requests.get(url=f"https://jsonplaceholder.typicode.com/users/{param}")
    responce = responce.json()
    name = responce.get('name')

    second_responce = requests.get(url=f"https://jsonplaceholder.typicode.com/users/{param}/todos")
    second_responce = second_responce.json()
    for todos in second_responce:
        total_todos += 1
        if todos.get('completed') is True:
            done_todos += 1
            todos_title.append(todos.get('title', 'not found'))

    print('Employee {} is done with tasks({}/{}):'.format(
        name,
        done_todos,
        total_todos
    ))

    for title in todos_title:
        print('\t ' + title)
