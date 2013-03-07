import os
import os.path
import shutil


# This is used to determine whether the string starts with something
# print astring.startswith("Hello")

"""
create 26 directories in the current directory, one for each letter of the alphabet, './a/'
loop through all files in original_files directory
organize files into the directory that their name starts with

"""

folders = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

# while len(folders):
for f in folders:
    files = os.listdir("original_files/files")

    for filename in files:
        if filename.startswith(f):
            if os.path.exists("/home/user/src/wk1_day3/Week_1_Project/" + f):
                shutil.copy2("original_files/files/" + filename,
                    "/home/user/src/wk1_day3/Week_1_Project/" + f)
            else:
                shutil.move("original_files/files/" + filename,
                    "/home/user/src/wk1_day3/Week_1_Project/" + f)

# Change the current working directory to path.
# os.chdir(path)

#shutil.move(src, dst)

# os.chdir("/home/user/src/wk1_day3/Week_1_Project/a")