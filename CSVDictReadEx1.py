#Program for reading csv file (MS-Excel) Data in the form of Dict
import csv
try:
    with open("C:\\Users\\MANDALA SHIRISHA\\Files6pm\\student1.csv")as fp:
        csvdr=csv.DictReader(fp) #csvdr is an object of class- csv.DictReader
        for record in csvdr: #record is an object of Dict
            print("---------------------")
            for k,v in record.items():
                print("\t{}\t{}".format(k,v))
            print("-----------------------------")
except FileNotFoundError:
    print("File does not exist")