try:
    fp=open("student.data")
except FileNotFoundError:
    print("File does not exist")
else:
    filedata=fp.readlines()
    print("--------------------")
    for val in filedata:
        print(val,end="")
    print("--------------------")