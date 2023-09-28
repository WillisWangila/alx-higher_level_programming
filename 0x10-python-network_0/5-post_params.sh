#!/bin/bash
#Takes url, sends POST request with variable email and subject and displays response, uses curl
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
