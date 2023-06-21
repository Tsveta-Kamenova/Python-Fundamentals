data = input()
list_input = []
dict_phones = {}


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


while data != "Over":
    list_input = data.split(" : ")
    name = list_input[0]
    number = list_input[1]

    if not is_int(name):
        dict_phones[name] = number
    else:
        dict_phones[number] = name

    data = input()


for item in sorted(dict_phones.keys()):
    print(f"{item} -> {dict_phones[item]}")