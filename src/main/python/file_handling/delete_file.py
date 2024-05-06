# Importing operating system module
import os
# Check if the file exists in the specified path/directory
if os.path.exists("text_file_io.txt"):
    os.remove("text_file_io.txt")
else:
    print("The file does not exist")

# Trying to open a deleted file causes an error
# Uncomment the following line to observe the error
# f_object = open("text_file_io.txt")