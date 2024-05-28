#!/usr/bin/python3
""" post an email 1 """
import requests
import sys

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=data)
    print(response.text)
