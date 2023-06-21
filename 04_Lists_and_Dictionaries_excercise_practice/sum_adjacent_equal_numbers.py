input_list = list(map(float, input().split(" ")))
sum_adjacent = 0
index = 0


while True:
    if input_list[index] == input_list[index+1]:
        sum_adjacent = input_list[index] + input_list[index+1]
        input_list.pop(index)
        input_list.pop(index)
        input_list.insert(index, sum_adjacent)
        index = 0
    else:
        index += 1

    if index+1 == len(input_list) or len(input_list) == 1:
        break

print(*input_list)
