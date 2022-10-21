#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    username = argv[1]
    # in your case, a personal access token as password
    password = argv[2]
    req = requests.get('https://api.github.com/user',
                       auth=(username, password))
    if req.status_code == 200:
        print(req.json().get('id'))
    else:
        print('None')
