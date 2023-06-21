base = float(input())
height = float(input())
area = None


def triangle_area(b, h):
    area = h*b/2
    return area


print(f"{triangle_area(base, height):.12g}")