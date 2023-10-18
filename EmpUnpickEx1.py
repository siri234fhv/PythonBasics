#Unpickling
import pickle
def reademprecords():
    try:
        with open("emp.pick","rb") as fp:
            print("--------------------")
            while(True):
                try:
                    record=pickle.load(fp)
                    for val in record:
                        print("{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("--------------")
                    break
    except FileNotFoundError:
        print("File doesn't exist:")
#main prog
reademprecords()
