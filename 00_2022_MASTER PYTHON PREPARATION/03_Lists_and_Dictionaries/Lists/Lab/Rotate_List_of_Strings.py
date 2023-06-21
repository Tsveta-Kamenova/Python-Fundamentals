list_input = list(input().split(" "))
rotated_list = [list_input[-1]]

rotated_list += list_input[:-1]

print(*rotated_list)
