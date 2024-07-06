#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter."""

from sys import argv
import requests

if __name__ == "__main__":
    if (len(argv) == 1):
        letter = ""
    else:
        letter = argv[1]
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', {"q": letter})
        if(r.json):
            print("[{}] {}".format(r.get("id")), r.get("name"))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
