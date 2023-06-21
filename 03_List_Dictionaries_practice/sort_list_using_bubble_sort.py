input_list = list(map(int, input().split(" ")))
pass_num = 0
bubble_list = 0

for pass_num in range(len(input_list)-1, 0, -1):
    for i in range(pass_num):
        if input_list[i] > input_list[i+1]:
            bubble_list = input_list[i]
            input_list[i] = input_list[i+1]
            input_list[i+1] = bubble_list
print(*input_list)