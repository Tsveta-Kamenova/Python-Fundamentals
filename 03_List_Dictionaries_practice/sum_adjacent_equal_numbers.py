input_list = list(map(float,input().split(" ")))

hope_list = input_list
n = len(input_list)
a = 0
b = 1


# for index in range (0, n-1):
while b<n:
    if input_list[a] == input_list[b]:
        hope_list[b] = input_list[a]+input_list[a]
        hope_list.pop(a)
        a = 0
        b = 1
    else:
        a += 1
        b += 1
    n = len(hope_list)

print(hope_list)

