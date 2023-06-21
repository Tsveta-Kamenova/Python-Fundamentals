input_key = input()
input_value = input()
input_n = int(input())

dict_values = {}
list_correct_values = []


for i in range(0, input_n):
    input_list = input().split(" => ")
    input_key_to_check = input_list[0]
    input_value_to_check = input_list[1].split(";")

    if input_key in input_key_to_check:
        list_correct_values = [item for item in input_value_to_check if input_value in item]

        dict_values[input_key_to_check] = list_correct_values


for item in dict_values:
    print(f"{item}:")
    for j in dict_values[item]:
        print(f"-{j}")
