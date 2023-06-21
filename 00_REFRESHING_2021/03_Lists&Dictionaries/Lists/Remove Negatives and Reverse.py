numbers = list(map(int, input().split(" ")))

positive_list = []

for item in numbers:
    if item > 0:
        positive_list.append(item)

positive_list.reverse()

if not len(positive_list) == 0:
    print(*positive_list)
else:
    print("empty")

