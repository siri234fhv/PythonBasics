filename=input("Enter any File Name:")
try:
    with open(filename,"r")as fp:
        filedata=fp.readlines()
        nl=0
        nw=0
        nch=0
        for line in filedata:
            nl=nl+1
            nw=nw+len(line.split())  #"python Progr"# result "python","Prog"
            nch=nch+len(line)
        else:
            print("-------------------------")
            print("Number of lines=",nl)
            print("Number of words=",nw)
            print("Number of Chars=",nch)
            print("---------------------------")
except FileNotFoundError:
    print("File does not exist")
