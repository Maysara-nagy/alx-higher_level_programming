#!/usr/bin/python3
"""a Python script that takes 2 arguments
    in order to solve this challenge."""

from sys import argv
import requests

if __name__ == "__main__":
    repoName = argv[1]
    ownerName = argv[2]

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(ownerName, repoName))
    try:
        for index in range(10):
            print("{}: {}".format(
                r.json()[index].get("sha"),
                r.json()[index].get("commit").get("author").get("name")))
    except IndexError:
        pass
