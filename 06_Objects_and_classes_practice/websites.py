class Websites:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries


data = input()
list_websites = []

while data != "end":
    split_data = data.split(" | ")
    h = split_data[0]
    d = split_data[1]
    if len(split_data) > 2:
        q = split_data[2].split(",")
    else:
        q = ""

    current_website = Websites(h, d, q)
    list_websites.append(current_website)

    data = input()

for w in list_websites:
    print(f"https://www.{w.host}.{w.domain}", end="")

    if not w.queries == "":
        print("/query?=[", end="")
        print(*w.queries, sep="]&[", end="")
        print("]")
    else:
        print("")

