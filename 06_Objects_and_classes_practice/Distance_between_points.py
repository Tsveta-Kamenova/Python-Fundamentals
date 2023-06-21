import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(a, b):
    c = math.sqrt(a**2 + b**2)
    return c


data_first_point = list(map(float, input().split()))
data_second_point = list(map(float, input().split()))

first_x = data_first_point[0]
second_x = data_second_point[0]
first_y = data_first_point[1]
second_y = data_second_point[1]

first_point = Point(x=first_x, y=first_y)
second_point = Point(x=second_x, y=second_y)

side_a = abs(first_point.x - second_point.x)
side_b = abs(first_point.y - second_point.y)

side_c = calc_distance(side_a, side_b)

print(f'{side_c:.3f}')
