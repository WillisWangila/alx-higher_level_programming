#!/bin/bash
#Makes a request to sanndbox to make it respond with "You got me", use curl
curl -s --location -X PUT -H "Origin: School" -d "user_id=98"  http://3cc921150c38.06a715d8.alx-cod.online:5000/catch_me
