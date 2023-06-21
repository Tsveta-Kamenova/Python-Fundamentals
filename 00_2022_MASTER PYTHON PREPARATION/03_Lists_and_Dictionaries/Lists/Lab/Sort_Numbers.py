list_input = list(map(int, input().split(" ")))

list_input.sort()
s = " <= "

s = s.join(map(str, list_input))

print(s)