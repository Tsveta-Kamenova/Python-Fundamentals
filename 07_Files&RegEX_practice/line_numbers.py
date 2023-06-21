counter = 0
list_rows = []
with open("file_to_read.txt", "r") as r_file:
    rows = r_file.readlines()
    for row in rows:
        list_rows.append(row)

with open("file_to_write2.txt", "w") as w_file:
    for row in rows:
        counter += 1
        a = str(counter) + "." + row
        w_file.write(a)