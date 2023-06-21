data_list = list(map(float, input().split(" ")))
data_dict = {}

for item in data_list:
    if item in data_dict:
        data_dict[item] += 1
    else:
        data_dict[item] = 1

for item in sorted(data_dict.keys()):
    if item - int(item) == 0:
        print(f"{item} -> {data_dict[item]} times")
    else:
        print(f"{item} -> {data_dict[item]} times")