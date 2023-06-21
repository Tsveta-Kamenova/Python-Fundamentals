def calc_triangle_area(base, height):
    area = base*height/2
    return area


b = float(input())
h = float(input())

result = calc_triangle_area(b, h)

print(f"{result:.12g}")
