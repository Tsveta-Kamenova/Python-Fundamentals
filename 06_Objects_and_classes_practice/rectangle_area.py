class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        area = self.width*self.height
        return area


data = list(map(float, input().split()))
w = data[0]
h = data[1]

my_rectangle = Rectangle(width=w, height=h)
print(my_rectangle.calc_area())


