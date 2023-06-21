data = input()
list_input = list(map(int, data.split()))
new_list = []
counter = 0

while data != "end":
    current_command = data.split(" ")
    if "swap" in current_command:
        a = int(current_command[1])
        b = int(current_command[2])
        length = len(list_input)
        if length > a >= 0 and length > b >= 0:
            list_input[a], list_input[b] = list_input[b], list_input[a]
        print(list_input)
        counter += 1
    if "enumerate_list" in current_command:
        print(list(enumerate(list_input)))
        counter += 1
    if "max" in current_command:
        print(max(list_input))
        counter += 1
    if "get_divisible" in current_command and int(current_command[2]):
        num = int(current_command[2])
        for item in list_input:
            if item % num == 0:
                new_list.append(item)
        print(new_list)
        new_list = []
        counter += 1
    if "min" in current_command:
        print(min(list_input))
        counter += 1
    else:
        pass
    data = input()

print(counter)