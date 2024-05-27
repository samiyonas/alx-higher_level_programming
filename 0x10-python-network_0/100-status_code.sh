#!/bin/bash
# only status code
curl -o /dev/null -sL -w "%{http_code}" $1
