list_input = input().split(" ")
integer = int(input())
new_list = []

for item in list_input:
    item = int(item)
    new_list.append(item*integer)

print(*new_list)