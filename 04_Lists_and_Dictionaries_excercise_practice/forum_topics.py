data = input()

dict_forum_topic = {}
dict_true = {}

list_result = []
list_tags = []


while data != "filter":
    list_data = data.split(" -> ")
    topic = list_data[0]
    tags = list_data[1].split(", ")

    if topic in dict_forum_topic:
        for item in tags:
            list_tags = list(dict_forum_topic[topic])
            if item in list_tags:
                pass
            else:
                dict_forum_topic[topic].extend(tags)
    else:
        dict_forum_topic[topic] = tags

    data = input()

data = input()

list_topics = data.split(", ")

for item in dict_forum_topic:
    list_values = list(dict_forum_topic[item])
    result = all(elem in list_values for elem in list_topics)
    if result:
        print(f"{item} | #", end="")
        print(", #".join(list_values))

