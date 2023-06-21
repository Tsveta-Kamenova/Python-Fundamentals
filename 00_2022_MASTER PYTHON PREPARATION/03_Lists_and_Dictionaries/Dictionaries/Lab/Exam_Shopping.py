data = input()
dict_inventory = {}

while data != "shopping time":
    data_split = list(data.split(" "))

    product_in_stock = data_split[1]
    quantity_in_stock = int(data_split[2])

    if product_in_stock not in dict_inventory:
        dict_inventory[product_in_stock] = quantity_in_stock
    else:
        dict_inventory[product_in_stock] += quantity_in_stock

    data = input()


while data != "exam time":
    data_split = list(data.split(" "))

    if data == "shopping time":
        data_split.pop()
        data_split.pop()
    else:
        product_to_buy = data_split[1]
        quantity_to_buy = int(data_split[2])

        if product_to_buy in dict_inventory:

            if dict_inventory[product_to_buy] <= 0:
                print(f"{product_to_buy} out of stock")

            else:
                dict_inventory[product_to_buy] -= quantity_to_buy

                if dict_inventory[product_to_buy] < 0:
                    dict_inventory[product_to_buy] = 0
        else:
            print(f"{product_to_buy} doesn't exist")

    data = input()

for item in dict_inventory:
    if dict_inventory[item] != 0:
        print(f"{item} -> {dict_inventory[item]}")
