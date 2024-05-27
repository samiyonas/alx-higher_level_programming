#!/bin/bash
# curl only methods
curl -sIL $1 | grep "Allow" | cut -d " " -f 2-
