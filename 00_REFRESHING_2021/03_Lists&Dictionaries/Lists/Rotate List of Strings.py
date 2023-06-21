list_input = list(map(str, input().split(" ")))
last_item = list_input.pop()

new_list = [last_item]

for item in list_input:
    new_list.append(item)

print(*new_list)

