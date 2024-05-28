#!/usr/bin/python3
""" what my status 1 """
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.encoding)))
    print("\t- content: {}".format(response.text))
