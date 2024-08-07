#!/usr/bin/python3
"""a Python script that takes in a URL, sends A request to the URL and displays
   the value of the X-Request-Id variable found in the header of the
   response."""

from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
