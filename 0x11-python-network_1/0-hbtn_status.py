#!/usr/bin/python3
""" Uses urllib to fetch a page"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as body:
        body = body.read()
    print("Body response:")
    print("- type:", type(body))
    print("- content:", body)
    print("- utf8 content:", body.decode('utf-8'))
