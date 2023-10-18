#Program for creating a folder hierarchy
import os
try:
    os.makedirs("c:\\HYD")
    print("Folders hierarchy created")
except FileExistsError:
    print("Folders hierarchy Already exist")