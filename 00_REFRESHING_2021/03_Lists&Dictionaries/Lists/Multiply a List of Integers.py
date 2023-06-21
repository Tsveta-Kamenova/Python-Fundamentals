numbers = list(map(int, input().split(" ")))
integer_to_multiply = int(input())

multiplied_list = []

for item in numbers:
    new_item = item*integer_to_multiply
    multiplied_list.append(new_item)

print(" ".join(map(str, multiplied_list)))