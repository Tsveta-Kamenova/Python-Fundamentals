lists = input().split("|")
new_list = []

for item in lists:
    a = item.split()
    new_list.append(a)

new_list.reverse()

new_list = filter(None, new_list)

for item in new_list:
    for i in item:
        print(f"{i}", end=" ")



