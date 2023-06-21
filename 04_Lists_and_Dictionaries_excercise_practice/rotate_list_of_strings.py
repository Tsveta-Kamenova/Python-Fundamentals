list_input = list(input().split(" "))

popped_list = list(list_input.pop().split(" "))

rotated_list = popped_list + list_input

print(*rotated_list)
