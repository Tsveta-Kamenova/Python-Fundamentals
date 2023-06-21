input_list = list(input())

dict_input = {}
for character in input_list:
    dict_input[character] = input_list.count(character)

for item in dict_input:
    print(f"{item} -> {dict_input[item]}")