filename=input("Enter any file name:")
try:
    with open(filename,"rt") as fp:
        filedata=fp.read()
        if(len(filedata)==0):
            print("File is Empty")
        else:
            print("-------------")
            print(filedata)
            print("---------------")
except FileNotFoundError:
    print("File does not exist")