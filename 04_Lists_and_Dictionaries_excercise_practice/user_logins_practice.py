data = input()

name_dict = {}
input_dict = {}


data_list = []
input_list = []

result = 0
result_name = 0
result_pass = 0

while data != "login":
    data_list = list(data.split(" -> "))

    name = data_list[0]
    pass_word = data_list[1]

    name_dict[name] = pass_word

    data = input()

while data == "login":
    pass
    data = input()

while data != "end":
    input_list = list(data.split(" -> "))

    input_name = input_list[0]
    input_pass = input_list[1]

    input_dict[input_name] = input_pass

    if input_name in name_dict and input_dict[input_name] == name_dict[input_name]:
        print(f"{input_name}: logged in successfully")
    if input_name not in name_dict:
        result_name += 1
        print(f"{input_name}: login failed")
    elif input_name in name_dict and input_dict[input_name] != name_dict[input_name]:
        result_pass += 1
        print(f"{input_name}: login failed")

    data = input()

result = result_name+result_pass

print(f"unsuccessful login attempts: {result}")
