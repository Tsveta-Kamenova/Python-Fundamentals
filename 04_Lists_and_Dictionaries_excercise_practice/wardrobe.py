n = int(input())

color = []
clothes = []
all_clothes = []

wardrobe = {}
number_clothes = {}
wardrobe_number_clothes = {}

number = 0

for i in range(0, n):
    data = input()

    data_list = list(data.split(" -> "))

    color = data_list[0]
    clothes = data_list[1].split(",")

    if color not in wardrobe:
        wardrobe[color] = clothes
    else:
        wardrobe[color] = wardrobe[color] + clothes

for item in wardrobe:
    number_clothes = {x: wardrobe[item].count(x) for x in wardrobe[item]}
    wardrobe_number_clothes[item] = number_clothes

data = input()

required = list(data.split(" "))
required_color = required[0]
required_clothes = required[1]

for color_clothes, type_clothes in wardrobe_number_clothes.items():
    print(f"{color_clothes} clothes: ")
    for key in type_clothes:
        if key == required_clothes and required_color == color_clothes:
            print("* " + key + " -", type_clothes[key], "(found!)")
        else:
            print("* " + key + " -", type_clothes[key])

