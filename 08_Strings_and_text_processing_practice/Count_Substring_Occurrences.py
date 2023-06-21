input_string = input().lower()
searched_string = input()
occurrences = 0
current_index = 0

while current_index != -1:
    current_index = input_string.find(searched_string.lower(), current_index)
    if current_index != -1:
        current_index += 1
        occurrences += 1

print(occurrences)
