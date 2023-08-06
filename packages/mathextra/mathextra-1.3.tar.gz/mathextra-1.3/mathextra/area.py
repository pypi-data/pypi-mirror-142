from math import tan
from __init__ import pi


def square_area(length):
    return length * length


def rectange_area(length, breadth):
    return length * breadth


def triange_area(base, height):
    return 0.5 * base * height


def regular_polygon_apothem(number_of_sides, lenght_of_each_side):
    return lenght_of_each_side / (2 * (tan(180 / number_of_sides)))


def regular_polygon_area(number_of_sides, length_of_each_side):
    apothem = length_of_each_side / (2 * (tan(180 / number_of_sides)))
    return (number_of_sides * length_of_each_side * apothem) / 2


def area_of_circle(radius):
    return radius * pi * 2
