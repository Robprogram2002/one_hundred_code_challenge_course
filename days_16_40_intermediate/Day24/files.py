# Reading Files

# one way is opening and closing the file manually

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# A better way is using the with context
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Writing to Files

# w mode will replace the content of the file with the new text
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# a mode will append the new text at the end
with open("my_file.txt", mode="a") as file:
    file.write("\nThis is a new line of text that will be appended at the end of the file")

# Opening a File that doesn't exit in write mode will create it from scratch

with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("New text.")
