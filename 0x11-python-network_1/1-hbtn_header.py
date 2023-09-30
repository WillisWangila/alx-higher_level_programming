#!/usr/bin/python3
"""sends a request to the url and shows the value
in the request_id"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        request_id = response.getheader('X-Request-Id')
    print(request_id)
