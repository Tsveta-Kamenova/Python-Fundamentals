list_input = list(map(int, input().split(" ")))
number = int(input())
n = len(list_input)
isFound = 0


for index in range(0, n):
    if number == list_input[index]:
        isFound = 1
    else:
        pass

if isFound:
    print("yes")
else:
    print("no")
