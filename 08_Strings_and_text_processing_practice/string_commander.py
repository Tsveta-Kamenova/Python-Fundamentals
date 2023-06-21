string_to_manipulate = input()
commands = input()

while commands != "end":
    if commands.startswith("Left"):
        count = int(commands[4:])
        for index in range(0, count):
            string_to_manipulate = string_to_manipulate[1:] + string_to_manipulate[0]

    if commands.startswith("Right"):
        count = int(commands[5:])
        for index in range(0, count):
            string_to_manipulate = string_to_manipulate[-1] + string_to_manipulate[:-1]

    if commands.startswith("Insert"):
        index_insert = int(commands.split()[1])
        string_to_insert = commands.split()[2]
        string_to_manipulate.insert(index_insert, string_to_insert)

    if commands.startswith("Delete"):
        start_index_delete = int(commands.split()[1])
        end_index_delete = int(commands.split()[2])
        string_to_manipulate = list(map(str, string_to_manipulate))
        string_to_manipulate[start_index_delete:end_index_delete+1] = []

    commands = input()

for item in string_to_manipulate:
    print(item, end="")