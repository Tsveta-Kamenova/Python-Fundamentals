list_employees = []


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


class Employee:
    def __init__(self, name, salary, position, age):
        self.name = name
        self.salary = salary
        self.position = position
        self.age = age


data = input()

while data != "filter base":
    age = None
    salary = None
    position = None

    input_list = list(data.split(" -> "))

    first = input_list[0]
    second = input_list[1]
    name = first

    if is_int(second):
        age = second
    elif is_float(second):
        salary = second
    elif is_str(second):
        position = second

    current_employee = Employee(name, salary, position, age)
    list_employees.append(current_employee)

    data = input()

data = input()

for item in list_employees:
    if data == "Position" and item.position is not None:
            print(f"Name: {item.name}")
            print(f"Position: {item.position}")
            print("====================")

    elif data == "Salary" and item.salary is not None:
            print(f"Name: {item.name}")
            print(f"Salary: {item.salary}")
            print("====================")

    elif data == "Age" and item.age is not None:
            print(f"Name: {item.name}")
            print(f"Age: {item.age}")
            print("====================")