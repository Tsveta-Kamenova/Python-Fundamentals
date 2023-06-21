input_list = list(map(int, input().split(" ")))

num = 0
n = len(input_list)

for num in range(0, n-1):
    for i in range(n-1, 0, -1):
        if input_list[i] < input_list[i-1]:
            input_list[i], input_list[i-1] = \
                input_list[i-1], input_list[i]

print(*input_list)