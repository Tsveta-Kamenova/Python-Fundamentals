banned_words = input().split()
input_string = input()

for item in banned_words:
    input_string = input_string.replace(item, "*"*len(item))

print(input_string)