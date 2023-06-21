import re

pattern = r"1(?<=1)0[C|D|H|S]|[2-9|A|J|K|Q][C|D|H|S]"

cards = input()

matches = re.finditer(pattern, cards)

for match in matches:
    print(match, end=" ")