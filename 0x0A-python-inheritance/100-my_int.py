#!/usr/bin/python3

""" A class that inherted int """


class MyInt(int):
    """ this class is supposed to rebel """
    def __eq__(self, other):
        """ checks for inequality

        Args:
            other (int instance) - to be compared to
        Returns:
            returns either True or False
        """
        if self.real != other:
            return True
        return False

    def __ne__(self, other):
        """ cheks for equality

        Args:
            other (int instance) - to be comapred to
        Returns:
            returns either True or False
        """
        if self.real == other:
            return True
        return False
