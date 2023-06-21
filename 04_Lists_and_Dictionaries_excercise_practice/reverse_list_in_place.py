input_list = list(map(int, input().split(" ")))

n = len(input_list)-1

for index in range(0, int(n/2)+1):
    input_list[index], input_list[n] = input_list[n],  input_list[index]
    n -= 1

print(*input_list)