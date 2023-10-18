import csv
try:
    with open("C:\\Users\\MANDALA SHIRISHA\\Files6pm\\emp.csv","r")as fp:
        csvr=csv.reader(fp) #csvr is an object of class,_csv.reader>
        for record in csvr: #record is an obj of class,'list'>
            for val in record:
                print("{}".format(val))
            print()
except FileNotFoundError:
    print("File does not exist")
