#!/usr/bin/python3
import requests
response = requests.head("https://httpbin.org/get")
print(response.history)
