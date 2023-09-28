#!/bin/bash
#Send a POST request with contents of a JSON file(2nd arg) to a given URL, returns body of response, use curl.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
