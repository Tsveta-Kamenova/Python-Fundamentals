data = input()
city_capacity = {}

while data != "ready":
    list_data = data.split(":")
    city = list_data[0]
    list_transport = list_data[1].split(",")

    if city not in city_capacity:
        city_capacity[city] = {}

    for item in list_transport:
        transport = item.split("-")[0]
        capacity = item.split("-")[1]
        city_capacity[city][transport] = capacity

    data = input()

data = input()

while data != "travel time!":
    city = data.split()[0]
    people = data.split()[1]

    result = 0
    for item in city_capacity[city]:
        result += int(city_capacity[city][item])

    people = int(people)
    if result >= people:
        print(f"{city} -> all {people} accommodated")
    else:
        print(f"{city} -> all except {people - result} accommodated")

    data = input()

