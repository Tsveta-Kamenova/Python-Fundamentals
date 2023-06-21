input_list = list(map(int, input().split(" ")))

n = len(input_list)-1
last_num = 0
a = 0
b = 1

for index in range(0, n):
    while input_list[b] < input_list[a]:
        input_list[a], input_list[b] = \
            input_list[b], input_list[a]
        last_num = input_list.index(input_list[a])

        for item in range (last_num, 0, -1):
            if input_list[item] < input_list[item-1]:
                input_list[item], input_list[item-1] = \
                    input_list[item-1], input_list[item]

    a += 1
    b += 1

print(*input_list)


