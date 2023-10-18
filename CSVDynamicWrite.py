import csv
noh=int(input("Enter how many header Names u have:"))
if(noh<=0):
    print("invalid Header Names")
else:
    hns=[] #empty list
    for i in range(1,noh+1):
        hn=input("Enter {} Header Name:".format(i))
        hns.append(hn)
        #accept number of records
    records=[]
    while(True):
            record=[]
            #accept the first header name value
            print("----------------------------")
            for i in range(0,len(hns)):
                hv1=input("Enter value for {}:".format(hns[i]))
                record.append(hv1)
            records.append(record)
            print("-----------------")
            ch=input("Do you want to enter another record(yes/no):")
            if(ch.lower()=="no"):
                break
            print("--------------------------------")
            #save records to the CSV file#
    with open("C:\\Users\\MANDALA SHIRISHA\\Files6pm\\Books.csv","w")as fp:
            csvwr=csv.writer(fp)
            csvwr.writerow(hns)
            csvwr.writerows(records)
            print("CSV File Created Dynamically--verify")