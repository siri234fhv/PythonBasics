#Program for creating CSV File
import csv #step  1
hn=["SNo","SName","Marks","Branch"] #step-2
records=[[100,"RS",300,"CSE"],
         [200,"RS",200,"CE"],
         [300,"RS",400,"EC"],
         [400,"RS",500,"MEC"],
         [500,"RS",600,"CS"]] #records Nested list
with open("C:\\Users\\MANDALA SHIRISHA\\Files6pm\\student1.csv","w")as fp: #step 3
    #step-4
    csvwr=csv.writer(fp) #here csvwr is an object of class _csv.write
    #step-5
    csvwr.writerow(hn) #writes header name to csv file
    #step-6
    csvwr.writerows(records) #writes records to CSV File
    print("CSV File Created --verify")
