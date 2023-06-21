data = input()

posts = {}

while data != "drop the media":
    command = data.split(" ")[0]
    post_name = data.split(" ")[1]

    if command == "post":
        posts[post_name] = {"Likes": 0, "Dislikes": 0, "Comments": {}}

    elif command == "like":
        posts[post_name]["Likes"] += 1

    elif command == "dislike":
        posts[post_name]["Dislikes"] += 1

    elif command == "comment":
        author = data.split(" ")[2]
        comment = data.split(" ")[3:]
        posts[post_name]["Comments"].update({author: comment})

    data = input()

for post_name, social_media_data in posts.items():
    print(f"Post: {post_name} ", end="")
    for key, value in social_media_data.items():
        if key == "Comments":
            print()
            print(f"Comments:")
            if value:
                for author, comment in value.items():
                    print(f"*  {author}: {' '.join(comment)}")
            else:
                print("None")
        else:
            print(f"| {key}: {value} ", end="")
