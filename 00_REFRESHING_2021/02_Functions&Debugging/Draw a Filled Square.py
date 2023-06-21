size_n = int(input())


def top_row(n):
    for i in range(n):
        print("-"*2, end="")
    print()


def middle_part(n):
    for i in range(0, n-2):
        print("-", end="")
        print("\\/"*(n-1), end="")
        print("-")


def bottom_row(n):
    for i in range(n):
        print("-"*2, end="")
    print()


top_row(size_n)
middle_part(size_n)
bottom_row(size_n)
