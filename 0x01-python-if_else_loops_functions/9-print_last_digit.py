#!/usr/bin/python3
def print_last_digit(number):
    tmp = number
    if tmp < 0:
        tmp = tmp * -1
    x = tmp % 10
    print(x, end="")
    return x
