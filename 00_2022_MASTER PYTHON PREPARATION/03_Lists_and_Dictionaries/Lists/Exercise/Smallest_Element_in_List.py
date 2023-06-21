list_input = list(map(int, input().split(" ")))
n = len(list_input)
index = 0

while n > 1:

    first_number = list_input[index]

    if list_input[index+1] < first_number:
        second_min_number = list_input[index+1]
        list_input[index] = second_min_number
        list_input[index+1] = first_number
        index = 0
    else:
        index += 1

    if index + 1 == n:
        break


print(list_input[0])