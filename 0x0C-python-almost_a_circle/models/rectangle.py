#!/usr/bin/python3

""" Rectangle class that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ create Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ automatically initializes Rectangle objects

        Args:
            width (int) - width of rectangle
            height (int) - height of rectangle
            x (any) - will document later
            y (any) - will document later
            id (int) - identity of the base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with char # """
        for j in range(self.__y):
            print(' ')
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """ formatted object print """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ update our attributes """
        if args and len(args) != 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                elif arg == 1:
                    self.width = args[arg]
                elif arg == 2:
                    self.height = args[arg]
                elif arg == 3:
                    selfi.x = args[arg]
                elif arg == 4:
                    self.y = args[arg]
                else:
                    break
        else:
            if kwargs and len(kwargs) != 0:
                for i in kwargs:
                    if i == "id":
                        self.id = kwargs[i]
                    elif i == "width":
                        self.width = kwargs[i]
                    elif i == "height":
                        self.height = kwargs[i]
                    elif i == "x":
                        self.x = kwargs[i]
                    elif i == "y":
                        self.y = kwargs[i]
                    else:
                        break
