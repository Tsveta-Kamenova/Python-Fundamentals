list_purged = []
list_lower = []
list_mixed = []
list_upper = []


list_data = input().replace(',', ' ').replace(';', ' ').replace(':', ' ').replace('.', ' ').replace('!', ' ').\
    replace('(', ' ').replace(')', ' ').replace('"', ' ').replace("'", ' ').replace('\\', ' ').replace('/', ' ').\
    replace("[']", ' ').replace("]", ' ').split(" ")


list_purged = [string for string in list_data if string != ""]


for item in list_purged:
    if item.isascii():
        if item.islower():
            list_lower.append(item)
        elif item.isupper():
            list_upper.append(item)
        else:
            list_mixed.append(item)

print("Lower-case: ", end="")
print(*list_lower, sep=", ")
print(f"Mixed-case: ", end="")
print(*list_mixed, sep=", ")
print(f"Upper-case: ", end="")
print(*list_upper, sep=", ")
