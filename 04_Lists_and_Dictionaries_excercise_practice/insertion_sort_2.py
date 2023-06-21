input_list = list(map(int, input().split(" ")))

n = len(input_list)
a = 0
b = 1
d = 0

if n == 2:
    while input_list[b] < input_list[a]:
        input_list[a], input_list[b] = \
            input_list[b], input_list[a]
elif n<2:
    pass

else:
    while True:
        while input_list[b] < input_list[a]:
            input_list[a], input_list[b] = \
                input_list[b], input_list[a]
            d += 1
            if b > 0 and a > 0:
                a -= 1
                b -= 1
        if d == 0:
            a += 1
            b += 1
        elif d + 2 < n and d != 0:
            a += d + 1
            b += d + 1
            d = 0
        elif d + 2 == n and d != 0:
            a += d
            b += d
            d = 0

        if b == n:
            break

print(*input_list)


