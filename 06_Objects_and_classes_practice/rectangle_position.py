class Rectangle:
    def __init__(self, left, top, width, height, right, bottom):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = right
        self.bottom = bottom


def is_inside(r1, r2):
    if (r1.left >= r2.left) and (r1.right <= r2.right) and (r1.top <= r2.top) and (r1.bottom <= r2.bottom):
        return "Inside"
    else:
        return "Not inside"


list_rectangles = []

for index in range(0, 2):
    data = list(map(float, input().split()))
    l = data[0]
    t = data[1]
    w = data[2]
    h = data[3]
    r = w+l
    b = t+h

    current_rectangle = Rectangle(top=t, left=l, width=w, height=h, right=r, bottom=b)
    list_rectangles.append(current_rectangle)

answer = is_inside(list_rectangles[0], list_rectangles[1])
print(answer)




