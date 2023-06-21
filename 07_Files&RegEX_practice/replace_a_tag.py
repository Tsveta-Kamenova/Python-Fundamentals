import re
new_tags = []
tags = input()

while tags != "end":
    replaced = re.sub("<a", "[URL", tags)
    replaced = re.sub("</a>", "[/URL]", replaced)
    replaced = re.sub("(>)(?=\w)", "]", replaced)
    new_tags.append(replaced)

    tags = input()

for item in new_tags:
    print(item, end="\n")