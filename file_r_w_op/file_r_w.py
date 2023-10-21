f = open("file_input.py", "w")  # create a file

f.write("print('suhail')")  # write the file
f.close()

with open("file_input.py", "r") as f:  # open the created file
    x = f.read()  # read the file

print(x)  # print the content of the file
# "w"is the write permission and "r" is the read permission
