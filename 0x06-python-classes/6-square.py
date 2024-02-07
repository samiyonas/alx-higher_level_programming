#!/usr/bin/python3

""" Define a Class """


class Square:
    """ A class that calculates area and uses property

    Attribute:
        __size (int) - private instance attribute(validated integer)
        __position (tuple) - private instance attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """ __init__ initializes objects

        Attribute:
            size (int) - will be validated to be assigned to __size
            position (tuple) - tuple optionally initialized to (0, 0)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter method

        Return:
            this method returns __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ position attribute getter method

        Return:
            return the tuple position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position attribute setter method """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ calculates area using __size

        Return:
            the method returns the square of __size attribute
        """
        return self.__size * self.__size

    def my_print(self):
        """ prints self.__size by self.__size of '#' """
        if not self.__size == 0:
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print("_", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
