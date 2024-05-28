#!/usr/bin/python3
""" fetch a url using urllib """
import urllib.request

req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    f = response.read()
print("Body response:")
print("\t- type: {}".format(type(f)))
print("\t- content: {}".format(f))
print("\t- utf8 content: {}".format(f.decode("utf-8")))
