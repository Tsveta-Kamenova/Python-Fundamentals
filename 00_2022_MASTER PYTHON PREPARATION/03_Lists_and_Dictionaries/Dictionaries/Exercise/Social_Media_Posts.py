raw_input = ()

dict_post = {}
list_database = []
dict_likes = {}
dict_dislikes = {}
dict_comments = {}


while raw_input != "drop the media":
    if raw_input.split()[0] == "post":
        current_post_name = raw_input.split()[1]
    elif raw_input.split()[0] == "like":
        current_like = raw_input.split()[1]
    elif raw_input.split()[0] == "dislike":
        current_dislike = raw_input.split()[1]
    elif raw_input.split()[0] == "comment":
        current_comment = raw_input.split()[1]






    raw_input = input()