data = input()
input_dict = {}


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


while data != "end":
    data_list = list(data.split(" = "))

    key_dict = data_list[0]
    value_dict = data_list[1]

    if is_int(value_dict) and value_dict not in input_dict.keys():
        input_dict[key_dict] = value_dict

    if value_dict in input_dict.keys():
        new_key_for_value = value_dict
        input_dict[key_dict] = input_dict[new_key_for_value]

    data = input()


for item in input_dict:
    input_dict[item] = int(input_dict[item])
    print(f"{item} === {input_dict[item]}")
