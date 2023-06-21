n = int(input())


def print_triangle(number):
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(f"{j} ", end="")
        print()
    for i in range(number-1, 0, -1):
        for j in range(1, i+1):
            print(f"{j} ", end="")
        print()


print_triangle(n)
