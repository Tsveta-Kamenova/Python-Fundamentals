n = int(input())

dict_clothes_color = {}
dict_clothes_number = {}
dict_clothes = {}

number_clothes = {}

for i in range(0, n):
    data = input()
    data_split = data.split(" -> ")

    color = data_split[0]
    clothes = data_split[1]
    clothes_list = clothes.split(",")

    if color in dict_clothes_color:
        new_clothes = clothes_list
        dict_clothes_color[color].extend(new_clothes)
    else:
        dict_clothes_color[color] = clothes_list

for item in dict_clothes_color:
#    number_clothes = {x: dict_clothes_color[item].count(x) for x in dict_clothes_color[item]}
    for x in dict_clothes_color[item]:
        number_clothes[x] = dict_clothes_color[item].count(x)
    dict_clothes[item] = number_clothes

data = input()

required = list(data.split(" "))
required_color = required[0]
required_clothes = required[1]

for color_clothes, type_clothes in dict_clothes.items():
    print(f"{color_clothes} clothes: ")
    for key in type_clothes:
        if key == required_clothes and required_color == color_clothes:
            print("* " + key + " -", type_clothes[key], "(found!)")
        else:
            print("* " + key + " -", type_clothes[key])