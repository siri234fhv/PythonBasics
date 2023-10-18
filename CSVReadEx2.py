import csv
try:
    with open("C:\\Users\\MANDALA SHIRISHA\\Files6pm\\student1.csv","r")as fp:
        csvr=csv.reader(fp)
        for record in csvr:
            for val in record:
                print("\t{}".format(val),end="")
        print()
except FileNotFoundError:
    print("File does not exist")