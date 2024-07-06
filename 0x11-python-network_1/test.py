#!/usr/bin/python3
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("http://python.org/")
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(response.decode('utf-8'))