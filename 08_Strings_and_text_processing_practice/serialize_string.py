def char_position(string, char):
    pos = []
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos


input_text = input()
unique = []
indexes = []

for item in input_text:
    if item not in unique:
        unique.append(item)

for letter in unique:
    print(f"{letter}:", end="")
    indexes = char_position(input_text, letter)
    indexes = "/".join(map(str, indexes))
    print(indexes)



