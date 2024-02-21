#!/usr/bin/python3

""" a function that writes to a file """


def write_file(filename="", text=""):
    """ writes and returns the number of chars """
    with open(filename, 'w', encoding="utf-8") as myfile:
        NumChars = myfile.write(text)
    return NumChars
