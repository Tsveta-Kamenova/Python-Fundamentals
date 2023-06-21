data = input().split(" ")

data_lower = []
dict_input = {}
list_output = []

for item in data:
    data_lower.append(item.lower())

#data_lower = [item.lower() for item in data]

for item in data_lower:
    if item not in dict_input:
        dict_input[item] = 1
    else:
        dict_input[item] += 1

for item in dict_input:
    if not dict_input[item] % 2 == 0:
        list_output.append(item)

print(", ".join(list_output))




