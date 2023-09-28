#!/bin/bash
#Sends delete request to url passed  as 1ST argument and displays response body, uses curl
curl -sX DELETE "$1"
