#def count_occurrences(lst, x):
#    count = 0
#    for element in lst:
#        if element == x:
#            count += 1
#        return count


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

for index in range(0, n-1):
    if list_input[index] == list_input[index+1]:
        counter += 1
        if index == n-2:
            print(f"{list_input[index]} -> {counter}")
    else:
        print(f"{list_input[index]} -> {counter}")
        counter = 1

if n == 1:
    print(*list_input, end="")
    print(" -> 1")
