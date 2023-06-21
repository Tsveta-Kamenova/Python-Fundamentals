list_input = input().split()
palindromes = []

for item in list_input:
    if item[::-1] == item[:]:
        palindromes.append(item)

print(", ".join(sorted(list(set(palindromes)))))

