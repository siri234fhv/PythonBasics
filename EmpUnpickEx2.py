#Reading the data from emp.pick
import pickle
def reademprecords():
    try:
        with open("emp.info","rb")as fp:
            print("---------------")
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print("{}".format(val),end="\t")
                print()
            except EOFError:
                print("------------------")
                break
    except FileNotFoundError:
        print("File does not exist")
#main memory
reademprecords()