indexes = []
dict_kv = {}
word = []
input_text = input()


while input_text != "end":
    letter = str(input_text[0])
    indexes = list(map(int, (input_text[2:].split("/"))))

    for item in indexes:
        dict_kv[item] = letter

    input_text = input()

for key, value in sorted(dict_kv.items()):
    print(f"{value}", end="")