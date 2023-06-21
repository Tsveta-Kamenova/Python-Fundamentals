list_shells = []
giant_shell_dict = {}
list_new = []


class Shell:
    def __init__(self, region, shell):
        self.region = region
        self.shell = shell


data = input()


while data != "Aggregate":
    data_list = list(data.split())

    region = data_list[0]
    shell = int(data_list[1])

    current_shell = Shell(region, shell)
    list_shells.append(current_shell)

    data = input()

for index in range(0, len(list_shells)-1):
    if list_shells[index].region == list_shells[index+1].region:
        giant_shell_sum = sum(p.shell for p in list_shells if p.region == list_shells[index].region)
        count_of_shells = sum(p.region == list_shells[index].region for p in list_shells)
        giant_shell = round((giant_shell_sum - giant_shell_sum/count_of_shells), 0)

    else:
        pass

    giant_shell_dict[list_shells[index].region] = giant_shell


for item in giant_shell_dict:

    print(f"{item} -> ", end="")

    for s in list_shells:
        if item == s.region:
            q = s.shell
            print(', '.join(q), end="")

    print(f"({giant_shell_dict[item]:.0f})")







