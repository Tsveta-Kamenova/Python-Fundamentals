list_input = list(map(int, input().split(" ")))

positive_list = []

for item in list_input:
    if item > 0:
        positive_list.append(item)

if not len(positive_list) == 0:
    print(*positive_list[::-1])
else:
    print("empty")