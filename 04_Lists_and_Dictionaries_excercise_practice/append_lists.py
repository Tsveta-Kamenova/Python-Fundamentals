input_list = list(input().split("|"))
work_list = []
n = len(input_list)
input_list.reverse()

for index in range(0, n):
    split_input = input_list[index].split(" ")
    work_list.extend(split_input)

for item in work_list:
    if item != "":
        print(item, end=" ")

