#!/usr/bin/python3

""" a class that inherits list """


class MyList(list):
    """ technically we're creating a list """
    def print_sorted(self):
        """ prints the sorted version of the list object """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
