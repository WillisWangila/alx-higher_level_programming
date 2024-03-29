#!/usr/bin/python3
"""
Sends POST request to http://0.0.0.0:5000/search_user with a given letter
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    try:
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': q}).json()
        if 'id' in response and 'name' in response:
            print(f'[{response["id"]}] {response["name"]}')
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
