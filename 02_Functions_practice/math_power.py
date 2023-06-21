n = float(input())
p = int(input())
result = None


def math_power(num,power):
    result = num
    for i in range (1,power):
        result = result*num
    return result


print(math_power(n,p))