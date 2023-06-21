data = input()
dict_output = {}
key_previous = None


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


while data != "end":
    data_list = list(data.split(" = "))

    key_in_dict = data_list[0]
    value_in_dict = data_list[1]

    if value_in_dict not in dict_output.keys() and is_int(value_in_dict):
        dict_output[key_in_dict] = value_in_dict

    elif not is_int(value_in_dict) and value_in_dict in dict_output.keys():
        key_previous = value_in_dict
        dict_output[key_in_dict] = dict_output[key_previous]

    data = input()

for item in dict_output:
    dict_output[item] = int(dict_output[item])
    print(f"{item} === {dict_output[item]}")