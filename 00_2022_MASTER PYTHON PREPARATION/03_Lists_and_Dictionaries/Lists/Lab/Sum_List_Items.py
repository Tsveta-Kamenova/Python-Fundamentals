number_items = int(input())
list_input = []

for item in range(0, number_items):
    list_input.append(int(input()))

sum_items = sum(list_input)

print(sum_items)

