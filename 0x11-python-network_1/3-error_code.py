#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib import request, error

if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
