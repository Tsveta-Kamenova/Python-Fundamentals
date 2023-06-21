data = list(map(float, input().split(" ")))
number_occurrences = {}

for item in data:
    if not item in number_occurrences:
        number_occurrences[item] = 1
    else:
        number_occurrences[item] += 1

sd = sorted(number_occurrences.items())

for k, v in sd:
    print(f"{k} -> {v} times")
