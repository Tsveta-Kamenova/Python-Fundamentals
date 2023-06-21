type_input = input()
thing_1 = input()
thing_2 = input()


def greater_value(typo, n1, n2):

    result = None

    if typo == "int":
        if int(n1) > int(n2):
            result = n1
        else:
            result = n2

    elif typo == "string" or typo == "char":
        if n1 > n2:
            result = n1
        else:
            result = n2

    return result


print(greater_value(type_input, thing_1, thing_2))
