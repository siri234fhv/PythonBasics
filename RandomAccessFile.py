with open("C:\\Users\\MANDALA SHIRISHA\\OneDrive\\Documents\\SiriPy\\sampledata","r")as fp:
    print("--------------------------------")
    print("Initial Index of fp=",fp.tell())
    filedata=fp.read(3)
    print(filedata)
    print("Now index of fp=",fp.tell())
    filedata=fp.read(7)
    print(filedata)
    print("Now index of fp=", fp.tell())
    print("-------------------------")
    filedata=fp.read()
    print(filedata)
    print("Now index of fp=", fp.tell())
    print("------------------------")
    #Reset fp to 150 index
    fp.seek(108)
    filedata = fp.read()
    print(filedata)
    # Reset fp to 0 index
    fp.seek(0)
    filedata = fp.read()
    print(filedata)
    fp.seek(108)
    filedata = fp.read()
    print(filedata)
    print("=======================")