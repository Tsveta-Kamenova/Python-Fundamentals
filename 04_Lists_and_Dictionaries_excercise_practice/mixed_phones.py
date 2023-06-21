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

    first_item = data_list[0]
    second_item = data_list[1]

    if is_int(first_item):
        dict_input[second_item] = first_item
    else:
        dict_input[first_item] = second_item

    data = input()

for item in sorted(dict_input.keys()):
    print(f"{item} -> {dict_input[item]}")

