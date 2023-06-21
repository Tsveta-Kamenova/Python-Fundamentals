j = input()


def is_integer(a):
    a = int(a)
    if type(a) is int:
        b = True
    else:
        b = False
    return b


print(is_integer(j))


