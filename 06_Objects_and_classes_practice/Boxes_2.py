from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def measure_distance(self, other_point):
        x = abs(self.x - other_point.x)
        y = abs(self.y - other_point.y)
        return sqrt(x**2 + y**2)


class Box:
    def __init__(self, u_l_p, u_r_p, b_l_p, b_r_p):
        self.u_l_p = u_l_p
        self.u_r_p = u_r_p
        self.b_l_p = b_l_p
        self.b_r_p = b_r_p
        self.width = Point.measure_distance(self.u_l_p, self.u_r_p)
        self.height = Point.measure_distance(self.u_l_p, self.b_l_p)
        self.perimeter = self.width*2 + self.height*2
        self.area = self.width*self.height


data = input()
list_boxes = []

while data != "end":
    upper_left = data.split(" | ")[0]
    upper_right = data.split(" | ")[1]
    bottom_left = data.split(" | ")[2]
    bottom_right = data.split(" | ")[3]

    upper_left_point = Point(int(upper_left.split(":")[0]), int(upper_left.split(":")[1]))
    upper_right_point = Point(int(upper_right.split(":")[0]), int(upper_right.split(":")[1]))
    bottom_left_point = Point(int(bottom_left.split(":")[0]), int(bottom_left.split(":")[1]))
    bottom_right_point = Point(int(bottom_right.split(":")[0]), int(bottom_right.split(":")[1]))

    current_box = Box(upper_left_point, upper_right_point, bottom_left_point, bottom_right_point)
    list_boxes.append(current_box)

    data = input()

for box in list_boxes:
    print(f"Box: {int(box.width)}, {int(box.height)}")
    print(f"Perimeter: {int(box.perimeter)}")
    print(f"Area: {int(box.area)}")


