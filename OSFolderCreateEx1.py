#Program for creating a folder
import os
try:
    os.mkdir("C:\\Python2")
    print("Folder Name created successfully")
except FileExistsError:
    print("File Already exist")
except FileNotFoundError:
    print("mkdir() can't create Folders Hierarchy")
