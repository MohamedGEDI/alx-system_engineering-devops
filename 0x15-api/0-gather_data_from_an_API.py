#!/usr/bin/python3
''' task 0 module'''


if __name__ == '__main__':
    import requests
    from sys import argv

    total_todos = 0
    done_todos = 0
    done_todos_titles = []

    res = requests.get(
                   'https://jsonplaceholder.typicode.com/users/')
    emp_name = res.json()
    print(emp_name[1])
