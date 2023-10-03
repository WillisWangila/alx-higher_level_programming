#!/usr/bin/python3
""" Uses urllib to fetch a page"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        response = response.read()
    print("Body response:")
    print("\t- type:", type(response))
    print("\t- content:", response)
    print("\t- utf8 content:", response.decode('utf-8'))
