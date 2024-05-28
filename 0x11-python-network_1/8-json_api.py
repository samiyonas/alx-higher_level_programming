#!/usr/bin/python3
""" search API """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        alpha = sys.argv[1]
    else:
        alpha = ""
    info = {"q": alpha}
    response = requests.post("http://0.0.0.0:5000/search_user", data=info)
    try:
        js = response.json()
        if not js:
            print("No result")
        else:
            print("[{}] {}".format(js.get("id"), js.get("name")))
    except ValueError:
        print("Not a valid JSON")
