#!/usr/bin/python3
"""
takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    link = 'https://api.github.com/users/{}'.format(argv[1])
    req = requests.get(link,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json().get('id'))
