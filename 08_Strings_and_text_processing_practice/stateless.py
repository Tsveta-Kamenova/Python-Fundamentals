input_text = input()
states = []

while input_text != "collapse":
    state = input_text
    fiction = input()

    state = state.replace(fiction, "")

    while len(fiction) > 0:
        fiction = fiction[1:-1]
        state = state.replace(fiction, "")

    if len(state) == 0:
        state = "(void)"

    states.append(state)

    input_text = input()

for item in states:
    print(f"{item.strip()}")

