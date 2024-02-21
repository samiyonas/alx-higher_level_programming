#!/usr/bin/python3

""" a function that appends to a file """


def append_write(filename="", text=""):
    """ appends to a file and returns Num of chars appended """
    with open(filename, 'a', encoding="utf-8") as myfile:
        CharAdded = myfile.write(text)
    return CharAdded
