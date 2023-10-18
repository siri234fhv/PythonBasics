#Program for listing the Files in folder
import os
try:
    FilesList=os.listdir("C:\\Users\\MANDALA SHIRISHA\\Data Types")
    print("----------------------------")
    for file in FilesList:
        print("\t{}".format(file))
except FileNotFoundError:
    print("File does not exist")