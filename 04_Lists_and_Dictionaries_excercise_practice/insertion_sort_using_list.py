input_list = list(map(int, input().split()))
output_list = []

output_list.append(input_list[0])

for index in range(1, len(input_list)):

    current_value = input_list[index]
    position = index

    while position > 0 and input_list[position - 1] > current_value:
        input_list[position] = input_list[position - 1]
        position = position - 1

        input_list[position] = current_value

    if current_value not in output_list:
        output_list.insert(position, input_list[position])

print(*output_list)
