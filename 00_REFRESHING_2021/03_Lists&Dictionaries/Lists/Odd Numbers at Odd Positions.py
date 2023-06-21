numbers = list(map(int, input().split(" ")))

for index in range (len(numbers)):
    if index % 2 == 1 and numbers[index] % 2 == 1:
        print(f"Index {index} -> {numbers[index]}")

