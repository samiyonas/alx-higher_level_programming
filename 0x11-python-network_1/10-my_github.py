#!/usr/bin/python3
""" api call to github api """
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
