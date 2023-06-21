num = int(input())


def print_top_bottom(n):
    print("-"*2*n)


def print_body(n):
    for i in range(0, n-2):
        print("-", end="")
        print("\/"*(n-1), end="")
        print("-", end="\n")


print_top_bottom(num)
print_body(num)
print_top_bottom(num)



