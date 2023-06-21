import math

import re


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(x1, y1, x2, y2):
    c = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return c


def calc_perimeter(a, b):
    perimeter = a*2 + b*2
    return perimeter


def calc_area(c, d):
    area = c*d
    return area


data = input()
list_points = []


while data != "end":
    split_data = re.split('[:|]', data)
    x1 = int(split_data[0])
    y1 = int(split_data[1])
    x2 = int(split_data[2])
    y2 = int(split_data[3])
    x3 = int(split_data[4])
    y3 = int(split_data[5])

    current_width = calc_distance(x1, y1, x2, y2)
    current_height = calc_distance(x1, y1, x3, y3)

    print(f"Box: {current_width:.0f}, {current_height:.0f}")
    print(f"Perimeter: {calc_perimeter(current_width, current_height):.0f}")
    print(f"Area: {calc_area(current_width, current_height):.0f}")

    data = input()
    