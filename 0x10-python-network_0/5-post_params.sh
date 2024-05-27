#!/bin/bash
# curl post parameters
email="test@gmail.com"
subject="I will always be here for PLD"
curl -sL -X "POST" -d "email=$email&subject=$subject" $1
