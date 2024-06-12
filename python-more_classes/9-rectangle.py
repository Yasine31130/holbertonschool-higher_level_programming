#!/usr/bin/python3
""" This module is a first creation of empty class for a rectangle """


class Rectangle():
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ init """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Func that returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Func that returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Func that returns the rectangle """
        rectstr = ""
        if self.__width == 0 or self.__height == 0:
            return rectstr
        else:
            for i in range(self.__height):
                for each in range(self.__width):
                    rectstr += str(self.print_symbol)
                if i < self.__height - 1:
                    rectstr += "\n"
        return rectstr

    def __repr__(self):
        """ Func that add repr """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ del """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """ square """
        return cls(size, size)
