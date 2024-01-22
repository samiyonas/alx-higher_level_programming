#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        string = ''
        for i in my_string:
            if i != 'c':
                string += i
        return string
