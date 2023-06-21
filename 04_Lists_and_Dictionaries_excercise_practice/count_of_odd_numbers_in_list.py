data_list = list(map(int, input().split(" ")))
count_odd = 0

for item in data_list:
    if not item % 2 == 0:
        count_odd += 1
    else:
        pass
print(count_odd)
