#!/usr/bin/python3

""" a function that reads a text file """


def read_file(filename=""):
    """ read file and print it out """
    with open(filename, 'r', encoding="utf-8") as myfile:
        f = myfile.read()
        print(f)
