list_input = list(map(int, input().split(" ")))
#print(min(list_input))
n = len(list_input)
smallest_item = list_input[0]

for i in range(0, n):
    if list_input[i] < smallest_item:
        smallest_item = list_input[i]
    else:
        pass

print(smallest_item)
