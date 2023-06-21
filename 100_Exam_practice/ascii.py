name = input()
result = 0

for item in name:
    result += ord(item)


print(result/100)

print(name.split())