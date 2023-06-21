import re


pattern = r"<\w*\d*\W*\w*>"

input_string = input()
matches = re.findall(pattern, input_string)
clean_matches = []


def sum_digits_string(string):
    sum_digit = 0
    for x in string:
        if x.isdigit():
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit


for item in matches:
    new_item = item[1:-1]
    clean_matches.append(new_item)

for item in clean_matches:
    print("Found "+str(sum_digits_string(item)) + " carat diamond")

if not clean_matches:
    print("Better luck next time")