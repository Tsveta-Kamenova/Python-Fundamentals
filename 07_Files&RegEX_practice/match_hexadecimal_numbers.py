import re

pattern = r"\b(0x)?[0-9A-F]+\b"

numbers = input()

matches = re.finditer(pattern, numbers)

for match in matches:
    print(match.group(), end=" ")