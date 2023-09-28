#!/bin/bash
# Accepts URL and displays all HTTP methods the server accepts, uses curl
curl -s --head "$1" | grep "Allow" | cut -c 8-
