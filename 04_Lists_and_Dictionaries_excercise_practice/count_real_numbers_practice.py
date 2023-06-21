data = list(map(float, input().split()))

dict_input = {}


for item in data:
    if item in dict_input:
        dict_input[item] += 1
    else:
        dict_input[item] = 1

for item in sorted(dict_input.keys()):
    if item - int(item) == 0:
        print(f"{int(item)} -> {dict_input[item]} times")
    else:
        print(f"{item} -> {dict_input[item]} times")
