import math

input_list = list(map(int, input().split(" ")))
result_list = []

for item in input_list:
    if item>0:
        if math.sqrt(item) == int(math.sqrt(item)) and item>0:
            result_list.append(item)
result_list.sort(reverse=True)
print(*result_list)
