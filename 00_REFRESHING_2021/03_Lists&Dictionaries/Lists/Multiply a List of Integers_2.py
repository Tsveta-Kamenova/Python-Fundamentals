list_input = input().split(" ")
integer_to_multiply = int(input())

multiplied_list = []
index = 0

for item in list_input:
    multiplied_list.append(int(item)*integer_to_multiply)
    print(multiplied_list[index], end=" ")
    index += 1

