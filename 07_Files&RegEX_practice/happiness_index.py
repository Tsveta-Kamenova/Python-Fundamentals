import re

pattern = r"(?P<happy_faces>[:|;][*D)\]}]|[*c(\[}][:|;])|(?P<sad_faces>[:|;][*Dc(\[{]|[*D)\]][:|;])"

count_happy = 0
count_sad = 0

faces = input()

matches = re.finditer(pattern, faces)

for match in matches:
    groups = match.groupdict()
    happy_faces = groups["happy_faces"]
    sad_faces = groups["sad_faces"]

    if happy_faces:
        count_happy += 1
    else:
        count_sad += 1
index = count_happy/count_sad

print(f"Happiness index: ", end="")
print("%.2f" % index, end=" ")
if index >= 2:
    print(":D")
elif 2 > index > 1:
    print(":)")
elif index == 1:
    print(":|")
elif index < 1:
    print(":(")

print(f"[Happy count: {count_happy}, Sad count: {count_sad}]")