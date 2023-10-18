try:
    with open("siri1.data","x+") as fp:
        print("File created and opened in write mode")
        print("Type of fp:",type(fp))
        print("File name:",fp.name)
        print("File mode:", fp.mode)
        print("Is File Readable=", fp.readable())
        print("Is File Writable=", fp.writable())
        print("Is File closed=", fp.closed)
        print("-------------------------------")
except FileExistsError:
    print("File already Exist")