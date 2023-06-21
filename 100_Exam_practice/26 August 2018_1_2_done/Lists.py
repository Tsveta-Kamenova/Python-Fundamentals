list_input = []
sum_unique_list = 0
sum_non_unique_list = 0


def make_unique(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y


data = input()

while data != "stop playing":
    list_input = list(map(int, data.split()))
    list_unique = list(map(int, make_unique(list_input)))

    if list_input == list_unique:
        for index in range(0, len(list_unique)):
            if list_unique[index] % 2 == 0:
                list_unique[index] += 2
            sum_unique_list += list_unique[index]
        list_unique.sort()
        print("Unique list: ", end="")
        print(",".join(map(str, list_unique)))
        b = sum_unique_list/len(list_unique)
        print(f"Output: ", end="")
        print("%.2f" % b)
        sum_unique_list = 0
    else:
        for index in range(0, len(list_input)):
            if list_input[index] % 2 != 0:
                list_input[index] += 3
            sum_non_unique_list += list_input[index]
        list_input.sort()
        a = sum_non_unique_list/len(list_input)
        print("Non-unique list: ", end="")
        print(":".join(map(str, list_input)))
        print(f"Output: ", end="")
        print("%.2f" % a)
        sum_non_unique_list = 0
    data = input()
