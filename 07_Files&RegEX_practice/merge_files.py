list_merged = []
with open("FileOne.txt") as textfile1, open("FileTwo.txt") as textfile2:
    for x, y in zip(textfile1, textfile2):
        x = x.strip()
        y = y.strip()
        list_merged.append(x + "\n")
        list_merged.append(y + "\n")
with open("FileMerge.txt", "w") as w_file:
    for item in list_merged:
        w_file.writelines(item)
