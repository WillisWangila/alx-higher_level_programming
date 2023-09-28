#!/bin/bash
#Sends request to url and displays ONLY status code of response, no redirection, use curl
curl -s -o /dev/null --write-out "%{http_code}" "$1"
