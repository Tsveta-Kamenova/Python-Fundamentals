import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Distance:
    def __init__(self, point_1, point_2, length):
        self.point_1 = point_1
        self.point_2 = point_2
        self.length = length


def calc_distance(x1, y1, x2, y2):
    c = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return c


number_of_points = int(input())

list_points = []
distances = []
min_distance = float("inf")

for index in range(0, number_of_points):
    current_point_input = list(map(int, input().split()))
    current_point = Point(current_point_input[0], current_point_input[1])
    list_points.append(current_point)

for i in range(len(list_points) - 1):
    for j in range(i + 1, len(list_points)):
        distance = Distance(point_1=list_points[i], point_2=list_points[j], length=calc_distance(list_points[i].x,
                                                                                                 list_points[i].y, list_points[j].x, list_points[j].y))
        distances.append(distance)

for i in range(0, len(distances)):
    if distances[i].length < min_distance:
        min_distance = distances[i].length
        point_1_min = distances[i].point_1
        point_2_min = distances[i].point_2
    else:
        pass

print(f"{min_distance:.3f}")
print(f"({point_1_min.x}, {point_1_min.y})")
print(f"({point_2_min.x}, {point_2_min.y})")



















