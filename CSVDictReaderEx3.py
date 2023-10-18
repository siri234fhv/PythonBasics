#Program for reading csv file (MS-Excel) Data in the form of Dict
import csv
try:
    with open("citizen.csv") as fp:
        csvdr=csv.DictReader(fp)
        for record in csvdr:
            print("----------------")
            for k,v in record.items():
                print("\t{}\t{}".format(k,v))
except FileNotFoundError:
    print("File does not exist")