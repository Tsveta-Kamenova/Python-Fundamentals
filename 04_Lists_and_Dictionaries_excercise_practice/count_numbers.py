input_list = list(map(int, input().split(" ")))

work_list = []
count_list = []

input_list.sort()

for item in input_list:
    if item not in work_list:
        work_list.append(item)

for item in work_list:
    item_count = input_list.count(item)
    count_list.append(item_count)

for index in range(len(work_list)):

    print(f"{work_list[index]} -> {count_list[index]}")
