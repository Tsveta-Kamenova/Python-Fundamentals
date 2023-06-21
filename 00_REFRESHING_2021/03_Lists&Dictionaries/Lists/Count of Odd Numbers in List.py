list_input = list(map(int, input().split(" ")))

count_odd_numbers = 0

for item in list_input:
    if not abs(item)%2 == 0:
        count_odd_numbers += 1

print(count_odd_numbers)

