#!/usr/bin/python3
""" list commits """
import requests
import sys

if __name__ == "__main__":
    header = {"Accept": "application/vnd.github+json"}
    response = requests.get(
            "https://api.github.com/repos/{}/{}/commits".
            format(sys.argv[2], sys.argv[1]), headers=header)
    for i in range(10):
        sha = response.json()[i].get("sha")
        auth = response.json()[i].get("commit").get("author").get("name")
        print("{}: {}".format(sha, auth))
