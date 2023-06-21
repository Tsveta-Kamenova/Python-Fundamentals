input_data = input()

dict_city = {}

name_city = str()
tourists = int()
capacity = int()

while input_data != "ready":

    raw_input = input_data.split(":")
    name_city = raw_input[0]
    list_vehicle_capacity = raw_input[1].split(",")

    if name_city not in dict_city:
        dict_city[name_city] = {}

    for item in list_vehicle_capacity:
        current_pair = item.split("-")
        current_vehicle = current_pair[0]
        current_capacity = int(current_pair[1])
        dict_city[name_city][current_vehicle] = current_capacity

    if input_data == "ready":
        break

    input_data = input()

while input_data != "travel time!":

    if "ready" in input_data:
        input_data = input()

    destination = input_data.split()[0]
    tourists = int(input_data.split()[1])

    capacity = 0

    for key in dict_city[destination]:
        capacity += dict_city[destination][key]

    difference = capacity - tourists

    if difference > 0:
        print(f"{destination} -> all {tourists} accommodated")
    else:
        print(f"{destination} -> all except {abs(difference)} accommodated")

    input_data = input()

