def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


dict_ref = {}

input_data = input()

while input_data != "end":
    first_key = input_data.split(" -> ")[0]
    second_part = input_data.split(" -> ")[1].split(", ")

    if is_int(second_part[0]):
        list_values = second_part
        if first_key not in dict_ref:
            dict_ref[first_key] = list_values
        else:
            dict_ref[first_key] += list_values

    elif second_part[0] not in dict_ref.keys() and not is_int(second_part[0]):
        pass

    else:
        second_key = second_part[0]
        new_list = list()
        for val in dict_ref[second_key]:
            new_list.append(val)
        dict_ref[first_key] = new_list

    input_data = input()

for item in dict_ref:
    print(f"{item} === ", end="")
    print(*dict_ref[item], sep=", ")