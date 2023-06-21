number_input = str(input())
sum_even = 0
sum_odd = 0


def multiply_even_odd(number):
    evens = 0
    odds = 0
    for item in number:
        if item.isdigit():
            item = int(item)
            if item % 2 == 0:
                evens += item
            else:
                odds += item
        else:
            pass
    result = evens * odds
    print(result)


multiply_even_odd(number_input)
