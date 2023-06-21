n = int(input())


def print_line(num):
    print("-"*2*num)

def print_body(num):
    for i in range(1,num-1):
        print("-"+"\\/"*(n-1)+"-")

print_line(n)
print_body(n)
print_line(n)

