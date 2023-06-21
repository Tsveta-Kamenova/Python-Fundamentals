input_list = list(map(int, input().split(" ")))
n = len(input_list)

for index in range(0, n):
    if index % 2 != 0 and input_list[index] % 2 != 0:
        print(f"Index {index} -> {input_list[index]}")