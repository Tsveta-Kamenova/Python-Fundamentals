data = input()

name_age = {}
name_salary = {}
name_position = {}

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_str(s):
    try:
        str(s)
        return True
    except ValueError:
        return False


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


while data != "filter base":

    input_list = list(data.split(" -> "))

    first = input_list[0]
    second = input_list[1]

    if is_int(second):
        name_age[first] = second
    elif is_float(second):
        name_salary[first] = second
    elif is_str(second):
        name_position[first] = second

    data = input()

data = input()

if data == "Position":
    for item in name_position:
        print(f"Name: {item}")
        print(f"Position: {name_position[item]}")
        print("====================")
elif data == "Salary":
    for item in name_salary:
        print(f"Name: {item}")
        print(f"Salary: {name_salary[item]}")
        print("====================")
elif data == "Age":
    for item in name_age:
        print(f"Name: {item}")
        print(f"Age: {name_age[item]}")
        print("====================")