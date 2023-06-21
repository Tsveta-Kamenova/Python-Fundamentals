list_input = list(map(int, input().split(" ")))
n = len(list_input)
list_indexes = []

for i in range(n):
    if not list_input[i] % 2 == 0 and not i % 2 == 0:
        list_indexes.append(i)

for item in list_indexes:
    print(f"Index {item} -> {list_input[item]}")