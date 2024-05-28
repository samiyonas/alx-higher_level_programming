#!/usr/bin/python3
""" post an email 0 """
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("utf-8")

    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as response:
        res = response.read()
        print(res.decode("utf-8"))
