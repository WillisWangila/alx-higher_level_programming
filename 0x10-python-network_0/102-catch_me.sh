#!/bin/bash
#Makes a request to sanndbox to make it respond with "You got me", use curl
curl -s --location -X PUT -H "Origin: School" -d "user_id=98"  0.0.0.0:5000/catch_me