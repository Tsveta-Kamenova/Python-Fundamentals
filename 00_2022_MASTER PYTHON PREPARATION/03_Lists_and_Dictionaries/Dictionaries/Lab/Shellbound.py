import math

dict_shells_separate = {}

list_shells = []

data_input = input()

while data_input != "Aggregate":
    list_input_shell = data_input.split(" ")
    city = list_input_shell[0]
    shells_number = int(list_input_shell[1])
    list_shells = [shells_number]

    if city not in dict_shells_separate:
        dict_shells_separate[city] = list_shells
    elif city in dict_shells_separate and shells_number not in dict_shells_separate[city]:
        dict_shells_separate[city].extend(list_shells)

    data_input = input()

for item in dict_shells_separate:
    x: int
    for x in dict_shells_separate[item]:
        sum_shells = sum(dict_shells_separate[item])
        count_shells = len(dict_shells_separate[item])
        average_shell = sum_shells - (sum_shells/count_shells)

    print(f"{item} -> ", end="")
    print(*dict_shells_separate[item], sep=", ", end=" ")
    print(f"({math.ceil(average_shell)})")
