#!/usr/bin/python3
from urllib.request import *



req = Request('http://www.python.org/fish.html')
try:
    urlopen(req)
except HTTPError as e:
    print(e.code)
    print(e.read())  
