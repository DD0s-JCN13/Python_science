lister = [1, 29, 53, 7, 16]
file_in = open("Testing.txt", "a")
for info in lister:
    file_in.write(str(lister.index(info)))
file_in.close()
file_read = open("Testing.txt", "r")
print(file_read.read())
file_read.close()