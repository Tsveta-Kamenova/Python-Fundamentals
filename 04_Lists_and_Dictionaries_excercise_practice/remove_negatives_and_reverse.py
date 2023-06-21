input_list = list(map(int, input().split(" ")))
n = len(input_list)

output_list = []

for index in range(0, n):
    if input_list[index] > 0:
        output_list.append(input_list[index])
        n -= 1
if output_list == []:
    print("empty")
else:
    output_list.reverse()
    print(*output_list)
