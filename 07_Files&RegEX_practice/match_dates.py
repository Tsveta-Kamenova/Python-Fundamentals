import re

pattern = r"\b(?P<day>\d{2})(?P<sep>[-.\/])(?P<month>\w{3})(?P=sep)(?P<year>\d{4})\b"

dates = input()

matches = re.finditer(pattern, dates)

for match in matches:
    groups = match.groupdict()
    day = groups["day"]
    month = groups["month"]
    year = groups["year"]
    print(f"Day: {day}, Month: {month}, Year:"
          f" {year}")