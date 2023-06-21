number = int(input())


def sign_of_integer(result):
    if number < 0:
        result = "negative"
    elif number > 0:
        result = "positive"
    else:
        result = "zero"
    return result


print(f"The number {number} is {sign_of_integer(number)}.")
