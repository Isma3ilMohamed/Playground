# The parameter mode can take the following values.
#
# x: This creates the file filename; it returns an error if the specified file already exists.
#
# r (default value): This opens a file to read its contents; it returns an error if the specified file doesn’t exist.
#
# a: This opens a file to append contents at its end; it creates the specified file if it doesn’t exist.
#
# w: This opens a file to write contents to it; it creates the file if it doesn’t exist.



# Read All File
# f_object = open("text_file_io.txt")
# print(f_object.read())
# f_object.close()

#############################################################


# Reading a specific number of characters from the file
# num_char = 7
# f_object = open("text_file_io.txt")
# print(f'\n\nReading first {num_char} characters:', f_object.read(num_char), '\n')
# f_object.close()


#############################################################


# Reading some lines from the file
# f_object = open("text_file_io.txt")
# print('\n\nReading a line:', f_object.readline(),
#       '\n\nReading another line:', f_object.readline())
# f_object.close()

#############################################################


# Looping through the file line by line
# print('\n\nLooping through the file line by line\n\n')
# f_object = open("text_file_io.txt")
# for x in f_object:
#     print(x)
# f_object.close()

#############################################################

# Use of with() along open for reading / writing tasks
print('\n\nUse of with() along open for reading / writing tasks\n\n')
with open("text_file_io.txt") as f_object:
    print(f_object.read())
f_object.close()
