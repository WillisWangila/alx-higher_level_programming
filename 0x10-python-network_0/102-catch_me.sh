#!/bin/bash
#Makes a request to sanndbox to make it respond with "You got me", use curl
curl -s --location -X PUT -H "Origin:School" -d "user_id=98"
