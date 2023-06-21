list_input = list(map(int, input().split(" ")))
counter_odd_numbers = 0

for item in list_input:
    if not item % 2 == 0:
        counter_odd_numbers += 1

print(counter_odd_numbers)