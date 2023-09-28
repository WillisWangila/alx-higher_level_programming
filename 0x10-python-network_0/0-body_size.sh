#!/bin/bash
# Sends request and displays size of response in bytes using curl
curl -s "$1" | wc -c
