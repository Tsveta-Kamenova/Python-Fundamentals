data = input()

dict_ref = {}
new_list = []

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


while data != 'end':
    list_data = data.split('->')
    key = list_data[0].strip()
    values = list_data[1].split(',')

    for value in values:
        value = value.strip()

        if key not in dict_ref.keys() and is_int(value):
            dict_ref[key] = [value]

        elif key in dict_ref.keys() and is_int(value):
            dict_ref[key].append(value)

        elif value not in dict_ref.keys() and not is_int(value):
            pass

        else:
            new_list = list()
            for val in dict_ref[value]:
                new_list.append(val)
            dict_ref[key] = new_list

    data = input()

for item in dict_ref:
    print(f"{item} === ", end="")
    print(", ".join(dict_ref[item]))
