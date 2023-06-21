import re


pattern = r"[a-zA-Z]"

input_string = input()
case_wanted = input()
list_needed = []
sum_letters = 0

letters_only_string = re.findall(pattern, input_string)


for item in letters_only_string:
    if case_wanted == "LOWERCASE" and item.islower() == 1:
        list_needed.append(item)
    elif case_wanted == "UPPERCASE" and item.isupper() == 1:
        list_needed.append(item)

for item in list_needed:
    sum_letters += ord(item)

print("The total sum is: "+str(sum_letters))

