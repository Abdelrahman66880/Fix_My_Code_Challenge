#!/usr/bin/python3
"""Square class to difen and determine the square properties"""


class Square():

    def __init__(self, width, height):
        self.width = width
        self.hieght = height

    def area_of_my_square(self):
        """Calculate the area of the square"""
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Calculate the permiter of the square"""
        return self.width * 4

    def __str__(self):
        return "{}/{}".format(self.width, self.hieght)


if __name__ == "__main__":
    s = Square(12, 12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
