data = input()
dict_input = {}


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


while data != "Over":
    data_list = list(data.split(" : "))

    key_dict = data_list[0]
    value_dict = data_list[1]

    if is_int(value_dict):
        dict_input[key_dict] = value_dict
    else:
        dict_input[value_dict] = key_dict

    data = input()


for item in sorted(dict_input.keys()):
    print(f"{item} -> {dict_input[item]}")
    