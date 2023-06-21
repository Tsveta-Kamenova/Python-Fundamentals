def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_str(s):
    try:
        str(s)
        return True
    except ValueError:
        return False


data = input()
dict_age = {}
dict_position = {}
dict_salary = {}


while data != "filter base":
    data_split = data.split(" -> ")

    a = data_split[0]
    b = data_split[1]

    if is_int(b):
        dict_age[a] = b
    elif is_float(b):
        dict_salary[a] = b
    elif is_str(b):
        dict_position[a] = b

    data = input()

data = input()

if data == "Position":
    for item in dict_position:
        print(f"Name: {item}")
        print(f"Position: {dict_position[item]}")
        print("====================")

elif data == "Salary":
    for item in dict_salary:
        print(f"Name: {item}")
        print(f"Salary: {dict_salary[item]}")
        print("====================")

elif data == "Age":
    for item in dict_age:
        print(f"Name: {item}")
        print(f"Age: {dict_age[item]}")
        print("====================")
