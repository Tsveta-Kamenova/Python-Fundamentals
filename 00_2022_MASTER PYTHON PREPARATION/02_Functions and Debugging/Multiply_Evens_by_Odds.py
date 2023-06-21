number_input = abs(int(input()))


def sum_odd_digits(a):
    sum_odd = 0
    for item in str(a):
        if not int(item) % 2 == 0:
            sum_odd += int(item)
    return sum_odd


def sum_even_digits(b):
    sum_even = 0
    for item in str(b):
        if int(item) % 2 == 0:
            sum_even += int(item)
    return sum_even


def multiplied_sum_of_digits(num):
    odd = sum_odd_digits(num)
    even = sum_even_digits(num)
    result = odd*even
    return result


print(multiplied_sum_of_digits(number_input))
