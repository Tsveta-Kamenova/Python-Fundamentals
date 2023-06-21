import re

pattern = r"\+359([- ])2\1\d{3}\1\d{4}\b"
phone_numbers = input()

matches = re.finditer(pattern, phone_numbers)

for match in matches:
    print(match.group(), end=" ")