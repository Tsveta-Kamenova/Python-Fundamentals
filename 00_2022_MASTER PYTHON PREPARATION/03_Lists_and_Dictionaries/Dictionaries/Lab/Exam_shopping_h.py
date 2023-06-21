result = {}
product = ''
quantity = 0
input_row = input()
while input_row != "shopping time":
    input_data = input_row.split(' ')
    product = input_data[1]
    quantity = int(input_data[2])
    if product in result:
        result[product] += quantity
    else:
        result[product] = quantity
    input_row = input()
input_row = input()
while input_row != "exam time":
    input_data = input_row.split(' ')
    product = input_data[1]
    quantity = int(input_data[2])
    if product in result:
        if result[product] <= 0:
            print("{0} out of stock".format(product))
        else:
            result[product] -= quantity
            if result[product] < 0:
                result[product] = 0
    else:
        print("{0} doesn't exist".format(product))
    input_row = input()

for key in result:
    if result[key] != 0:
        print("{0} -> {1}".format(key, result[key]))