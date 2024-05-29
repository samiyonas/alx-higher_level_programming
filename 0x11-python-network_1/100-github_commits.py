#!/usr/bin/python3
""" list commits """
import requests
import sys

if __name__ == "__main__":
    header = {"Accept": "application/vnd.github+json"}
    response = requests.get(
            "https://api.github.com/repos/{}/{}/commits".
            format(sys.argv[2], sys.argv[1]), headers=header)
    for i in response.json()[0:10]:
        sha = i.get("sha")
        auth = i.get("commit").get("author").get("name")
        print("{}: {}".format(sha, auth))
