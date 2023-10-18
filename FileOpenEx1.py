#By using open()
try:
    fp=open("stdu1.data")
except FileNotFoundError:
    print("File does not exist")
else:
    print("File open in Read mode Successfully")
    print("Type of fp=",type(fp))
    print("File Name:",fp.name)
    print("File Mode:",fp.mode)
    print("Is File Readable:",fp.readable())
    print("Is File writable:",fp.writable())
    print("Is FIle closes:",fp.closed)
finally:
    print("I am from finally block")
    fp.close()
    print("Is file closed=",fp.closed)
