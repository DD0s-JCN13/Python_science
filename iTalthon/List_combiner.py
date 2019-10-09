lister = [1, 29, 53, 7, 16]
file_in = open("Testing_text.txt", "a")
file_check = open("Testing_text.txt", "r")
if file_check.read() != "":
    file_in.write("\n")
    file_check.close()
else:
    file_check.close()
for info in lister:
    file_in.write(str(lister.index(info)))

file_in.close()
file_read = open("Testing_text.txt", "r")
print(file_read.read())
file_read.close()
