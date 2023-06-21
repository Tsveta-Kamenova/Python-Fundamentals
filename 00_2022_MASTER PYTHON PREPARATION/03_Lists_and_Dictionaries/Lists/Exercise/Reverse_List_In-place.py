list_input = list(map(int, input().split(" ")))
n = len(list_input)
m = int(n / 2)

for index in range(0, m):
    first_item = list_input[index]
    last_item = list_input[n - 1]
    list_input[index] = last_item
    list_input[n - 1] = first_item
    n -= 1

print(*list_input)

