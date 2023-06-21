data = list(map(str, input()))

dict_input = {}

for item in data:
    if item in dict_input:
        dict_input[item] += 1
    else:
        dict_input[item] = 1

for item in dict_input:
    print(f"{item} -> {dict_input[item]}")