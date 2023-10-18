x={10:"python",20:"Html",30:"C"}
with open("student1.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data written to the File")