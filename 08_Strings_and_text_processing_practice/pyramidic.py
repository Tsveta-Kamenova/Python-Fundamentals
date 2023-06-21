number_of_strings = int(input())
dict_letters_count = {}


for n in range(1, number_of_strings+1):

    current_string = input()

    counter = 1

    for i in current_string:
        if i not in dict_letters_count:
            dict_letters_count[i] = 1

        else:


print(max(dict_letters_count, key=dict_letters_count.get))
