import math


list_input = list(map(int, input().split(" ")))
list_square = []

for item in list_input:
    if item < 0:
        list_input.remove(item)

for item in list_input:
    if math.sqrt(item) == int(math.sqrt(item)):
        list_square.append(item)


list_square.sort(reverse=True)

print(*list_square)
