height = float(input())
base = float(input())


def triangle_area(a, h):
    area = a*h/2
    return area


result = triangle_area(height, base)

print(f"{result:.12g}")
