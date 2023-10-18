#Program for listing the Files in folder
import os
try:
    FilesList=os.listdir("C:\\Users\\MANDALA SHIRISHA\\Data Types")
    print("______________________")
    for file in FilesList:
        if(file.endswith(".py")):
            print("\t{}".format(file))
except FileNotFoundError:
    print("Folder does not exist")