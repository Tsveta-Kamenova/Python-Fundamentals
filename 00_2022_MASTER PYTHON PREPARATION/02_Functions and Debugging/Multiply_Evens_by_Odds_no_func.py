number_input = abs(int(input()))
sum_even = 0
sum_odd = 0


for item in str(number_input):
    if int(item) % 2 == 0:
        sum_even += int(item)
    else:
        sum_odd += int(item)

result = sum_even*sum_odd
print(result)

