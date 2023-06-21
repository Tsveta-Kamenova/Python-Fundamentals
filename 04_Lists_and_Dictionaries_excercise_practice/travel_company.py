class Travel:
    def __init__(self, name, vehicle, people):
        self.name = name
        self.vehicle = vehicle
        self.people = people


list_travel = []
list_unique = []
dict_needed = {}
dict_sum = {}

a = 0

data = input()

while data != "ready":
    input_list = data.split(":")

    name = input_list[0]
    transport = input_list[1].split(",")
    for index in range(0, len(transport)):
        new_trans = transport[index].split("-")
        vehicle = new_trans[0]
        people = int(new_trans[1])
        current_travel = Travel(name, vehicle, people)
        list_travel.append(current_travel)

    data = input()

for item in list_travel:
    for t in list_unique:
        if item.name == t.name and item.vehicle == t.vehicle:
            list_unique.remove(t)
    list_unique.append(item)

data = input()

while data != "travel time!":
    input_list_travel = data.split(" ")

    city_name = input_list_travel[0]
    people_needed = int(input_list_travel[1])
    dict_needed[city_name] = people_needed

    data = input()

list_unique.sort(key=lambda x: x.name, reverse=True)

#for item in list_unique:
    #print(f"{item.name} -> {item.vehicle} - {item.people}")

for index in range(0, len(list_unique)-1):
    if list_unique[index].name == list_unique[index+1].name:
        a = sum(p.people for p in list_unique if p.name == list_unique[index].name)
    else:
        a = list_unique[index+1].people
        if index == 0:
            a = list_unique[index].people
            dict_sum[list_unique[index].name] = a

    dict_sum[list_unique[index+1].name] = a


#print(f"{dict_needed}")

#print(f"{dict_sum}")

for k, v in dict_needed.items():
    if dict_sum[k] > dict_needed[k]:
        print(f"{k} -> all {dict_needed[k]} accommodated")
    elif dict_sum[k] < dict_needed[k]:
        b = dict_needed[k] - dict_sum[k]
        print(f"{k} -> all except {b} accommodated")

