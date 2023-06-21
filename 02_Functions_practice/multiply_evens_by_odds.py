number = int(input())


def multiply_evens_by_odds(n):
    #n = int(n)
    n = abs(n)
    #n = str(n)
    digit = 0
    sum_even = 0
    sum_odd = 0
    sum_product = 0

    while n>0:
        digit = n%10
        n = n//10
        if digit %2==1:
            sum_odd+=digit
        else:
            sum_even+=digit
    #for i in n:
        #i = int(i)
        #if i % 2 == 0:
         #   sum_even += i
        #else:
         #   sum_odd += i


        sum_product = sum_odd * sum_even
    return sum_product

print(multiply_evens_by_odds(number))