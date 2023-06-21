def compare_int(n1, n2):
    a = (n1, n2)
    result = max(a)
    return result


def compare_char(ch1, ch2):
    a = (ch1, ch2)
    result = max(a)
    return result


def compare_str(str1, str2):
    a = (str1, str2)
    result = max(a)
    return result


type_value = input()
first_value = input()
second_value = input()

if type_value == "int":
    print(compare_int(first_value, second_value))
elif type_value == "char":
    print(compare_char(first_value, second_value))
else:
    print(compare_char(first_value, second_value))
