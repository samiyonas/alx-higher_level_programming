#!/usr/bin/python3
def uppercase(str):
    tmp = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            tmp += chr(ord(i) - 32)
        else:
            tmp += i
    print("{}".format(tmp))
