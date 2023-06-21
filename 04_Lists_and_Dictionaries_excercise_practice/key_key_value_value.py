key_value_dict = {}

master_key = input()
master_value = str(input())
n = int(input())

list_values = []

for index in range(0, n):
    data = input()
    data_list = data.split(" => ")
    key = data_list[0]
    values_small = data_list[1].split(";")
    key_value_dict[key] = values_small


for key, value in key_value_dict.items():
    if master_key in key:
        print(f"{key}:")
        list_values.extend(value)

        for l in list_values:
            if master_value in l:
                print(f"-{l}")
                list_values = list_values[:0]


