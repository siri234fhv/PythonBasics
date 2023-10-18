#Reading the Data from the file
try:
    with open("student1.data")as fp:
        filedata=fp.read()
        print("------------")
        print(filedata)
        print("------------")
except FileNotFoundError:
    print("File does not exist")