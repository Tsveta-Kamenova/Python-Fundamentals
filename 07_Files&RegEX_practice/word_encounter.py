import re

list_words = []
new_list = []
list_answers = []
count = 0

task = input()

task_list = list(task)
letter = task_list[0]
number_of_times = int(task_list[1])

while task != "end":

    pattern = r"([A-Z][a-z]*)((?:\s?,*\s?'?)([a-z]+))*"
    matches = re.findall(pattern, task)
    list_words.append(matches)

    task = input()

for i in range(1, len(list_words)):
    new_list = list_words[i-1] + list_words[i]

for item in new_list:
    a = str(item)
    a = a.count(letter)
    if a == number_of_times:
        list_answers.append(item)

#print(", ".join(list_answers))
print(*matches)