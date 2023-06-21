input_list = list(map(int, input().split(" ")))

min_number = input_list[0]

for item in input_list:
    if item < min_number:
        min_number = item
print(min_number)