data = input()
dict_pass = {}
counter = 0

while data != "login":
    data_split = data.split(" -> ")
    username = data_split[0]
    password = data_split[1]

    if username not in dict_pass:
        dict_pass[username] = password

    data = input()

while data != "end":
    data_split = data.split(" -> ")

    if data == "login":
        data_split.pop()
    else:
        username_input = data_split[0]
        password_input = data_split[1]

        if username_input in dict_pass:
            if dict_pass[username_input] == password_input:
                print(f"{username_input}: logged in successfully")
            else:
                print(f"{username_input}: login failed")
                counter += 1
        else:
            print(f"{username_input}: login failed")
            counter += 1


    data = input()

print(f"unsuccessful login attempts: {counter}")