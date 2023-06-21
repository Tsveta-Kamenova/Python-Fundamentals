data_input = list(map(float, input().split(" ")))
new_number = 0
index = 0

while True:

    if data_input[index] == data_input[index+1]:
        new_number = data_input[index] + data_input[index+1]
        data_input.pop(index)
        data_input.pop(index)
        data_input.insert(index, new_number)
        index = 0
    else:
        index += 1

    if len(data_input) == 1 or index+1 == len(data_input):
        break

print(data_input)
