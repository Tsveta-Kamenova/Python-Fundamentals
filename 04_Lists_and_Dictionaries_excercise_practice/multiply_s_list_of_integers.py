data_list = list(map(int, input().split(" ")))
number = int(input())
output_list = []
new_number = 0

for item in data_list:
    new_number = item*number
    output_list.append(new_number)

print(*output_list)
