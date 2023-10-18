#Program for creating CSV File by using Dict data
import csv
hnames=["AdcNo","CName","City","Age"]
records=[{"adcno:123","cname:siri","city:Hyd","age:40"},
        {"adcno:234","cname:anu","city:Kurnool","age:47"},
        {"adcno:564","cname:Navya","city:Wgl","age:50"},
        {"adcno:457","cname:kavya","city:Hnk","age:60"}]
with open("citizen.csv","w") as fp:
    csvdwr=csv.DictWriter(fp,fieldnames=hnames)
    csvdwr.writeheader()
    csvdwr.writerows(records)
    print("CSv File Created with Dict Data--verify")