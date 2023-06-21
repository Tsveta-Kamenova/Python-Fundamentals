data = input()
list_stock = []
list_buy = []

dict_stock = {}
dict_buy = {}
dict_dont_exist = {}

while data != "shopping time":
    list_stock = data.split()
    stock = list_stock[1]
    count = int(list_stock[2])

    if stock in dict_stock.keys():
        dict_stock[stock] += count
    else:
        dict_stock[stock] = count

    data = input()

while data != "exam time":
    list_buy = data.split()
    if data == "shopping time":
        list_buy.pop()
        list_buy.pop()
    else:
        buy_thing = list_buy[1]
        buy_count = int(list_buy[2])
        if buy_thing not in dict_buy:
            dict_buy[buy_thing] = buy_count
        else:
            dict_buy[buy_thing] += buy_count
        if buy_thing not in dict_stock:
            dict_dont_exist[buy_thing] = buy_thing

    data = input()

for item in dict_dont_exist:
    print(f"{item} doesn't exist")

for item in dict_stock:
    if item in dict_buy:
        if dict_stock[item] < dict_buy[item]:
            print(f"{item} out of stock")
        elif dict_stock[item] == dict_buy[item]:
            pass
        else:
            new_stock = - dict_buy[item] + dict_stock[item]
            if new_stock == 0:
                pass
            else:
                print(f"{item} -> {new_stock}")
    else:
        print(f"{item} -> {dict_stock[item]}")
