list_input = list(map(int, input().split(" ")))
smallest_item = list_input[0]


for index in range(len(list_input)):
    if list_input[index] < smallest_item:
        smallest_item = list_input[index]

print(smallest_item)
