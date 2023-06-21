type = input()
value_1 = input()
value_2 = input()


def greater_value(t, v1, v2):
    result = None

    if t == "int" or t == "float":
        if v1 <= v2:
            result = v2
        else:
            result = v1
    elif t == "char":
        if ord(v1) <= ord(v2):
            result = v2
        else:
            result = v1
    elif t == "string":
        if v1 <= v2:
            result = v2
        else:
            result = v1
    return result


print(greater_value(type, value_1, value_2))
