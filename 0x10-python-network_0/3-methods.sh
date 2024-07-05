#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" 0.0.0.0:5000/route_4 | grep -i "Allow" | cut -d " " -f 2-
