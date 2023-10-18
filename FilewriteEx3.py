print("Enter the data and press '@' to stop")
with open("C:\\Users\\MANDALA SHIRISHA\\OneDrive\\Documents\\SiriPy\\sampledata","a")as fp:
    while(True):
        kbddata=input()
        if(kbddata!="@"):
            fp.write(kbddata+"\n")
        else:
            print("Data written to the file")
            break