#!/bin/bash
# curl a JSON file
curl -sL -X "POST" -H "Content-Type: application/json" --data @"./$2" $1
