#!/bin/bash
# Accepts url, sends a GET request with custom header and displays body of response, uses curl
curl -s -H "X-School-User-Id: 98" "$1"
