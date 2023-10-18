#Program for adding a new record to CSV File
import csv
record=[700,"SK",500,"CSV"]
with open("C:\\Users\\MANDALA SHIRISHA\\Files6pm\\student1.csv","a") as fp:
    csvwr=csv.writer(fp)
    print("type of csvwr=",type(csvwr))
    csvwr.writerow(record)
    print("Record added to CSV File--verify")
