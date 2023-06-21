input_list = list(map(str, input()))
number_occurences = {}

for item in input_list:
    if not item in number_occurences:
        number_occurences[item] = 1
    else:
        number_occurences[item] += 1

for item in number_occurences:
    print(f"{item} -> {number_occurences[item]}", end="\n")