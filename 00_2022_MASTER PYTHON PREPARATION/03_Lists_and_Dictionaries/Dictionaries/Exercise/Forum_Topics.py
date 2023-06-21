input_data = input()

dict_topics = {}
flag_bool = bool

while input_data != "filter":
    topic = input_data.split(" -> ")[0]
    tags = input_data.split(" -> ")[1].split(", ")

    if topic not in dict_topics:
        dict_topics[topic] = tags

    for i in tags:
        if i not in dict_topics[topic]:
            dict_topics[topic].append(i)

    input_data = input()

if input_data == "filter":
    pass

list_tags_to_print = input().split(", ")

for k, v in dict_topics.items():
    for item in list_tags_to_print:
        if item in dict_topics[k]:
            flag_bool = True
        else:
            flag_bool = False
            break

    if flag_bool:
        print(f"{k} | #", end="")
        print(*dict_topics[k], sep=", #")
