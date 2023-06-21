import re

pattern = r"(?P<tail>>*)<(?P<body>\(+)(?P<status>'|-|x)>"

fishes = input()
count = 1

matches = re.finditer(pattern, fishes)

if re.search(pattern, fishes) is None:
    print("No fish found.")

for match in matches:
    groups = match.groupdict()
    tail = groups["tail"]
    body = groups["body"]
    status = groups["status"]
    tail_length = len(tail)
    body_length = len(body)

    print(f"Fish {count}: ", end="")
    print(match.group())

    if status == "'":
        status_type = "Awake"
    elif status == "-":
        status_type = "Asleep"
    elif status == "x":
        status_type = "Dead"

    if tail_length > 5:
        tail_type = "Long"
    elif 1 < tail_length <= 5:
        tail_type = "Medium"
    elif tail_length == 1:
        tail_type = "Short"
    elif tail_length == 0:
        tail_type = "None"

    if body_length >= 10:
        body_type = "Long"
    elif body_length > 5:
        body_type = "Medium"
    else:
        body_type = "Short"

    count += 1

    if tail_type == "None":
        print(f"  Tail type: {tail_type}\n  Body type: {body_type} ({body_length*2} cm)\n  Status: {status_type}")
    else:
        print(
            f"  Tail type: {tail_type} ({tail_length * 2} cm)\n  Body type: {body_type} ({body_length * 2} cm)\n  Status: {status_type}")