list_input = input().split("|")
list_output = []

list_input.reverse()
n = len(list_input)

for i in range(n):
    list_output.extend(list_input[i].split(" "))

for item in list_output:
    if item != "":
        print(item, end=" ")
