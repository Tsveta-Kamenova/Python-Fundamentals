data = input().split(" ")
dict_input = {}


for item in data:
    if item.lower() in dict_input:
        dict_input[item.lower()] += 1
    else:
        dict_input[item.lower()] = 1

string_output = ""

for item in dict_input:
    if not dict_input[item] % 2 == 0:
        string_output+= item + ", "

print(string_output.strip(", "))

