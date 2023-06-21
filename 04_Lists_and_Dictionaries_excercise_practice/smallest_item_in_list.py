data_list = list(map(int, input().split(" ")))
n = len(data_list)
min_number = data_list[0]
for item in range (0,n):
    if data_list[item] < min_number:
        min_number = int(data_list[item])
print(min_number)