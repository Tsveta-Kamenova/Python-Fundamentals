input_list = list(map(int, input().split()))


for index in range(1, len(input_list)):

    current_value = input_list[index]
    position = index

    while position > 0 and input_list[position - 1] > current_value:
        input_list[position] = input_list[position - 1]
        position = position - 1

        input_list[position] = current_value

print(*input_list)
