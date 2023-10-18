#with open() as var:
with open("stdu1.data","w")as fp:
    print("File created and opened in write mode")
    print("Type pf fp=",type(fp))
    print("Type of File Name:",fp.name)
    print("Type of mode:",fp.mode)
    print("Is File Readable=",fp.readable())
    print("Is File Writable=", fp.writable())
    print("Is File closed=", fp.closed)
print("-----------------------------")
print("Is File Closed=", fp.closed)