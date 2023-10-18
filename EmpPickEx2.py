import pickle
def saveempdata():
    with open("emp.pick","ab")as fp:
        while(True):
            try:
                #read emp data from KBD
                print("-----------------------")
                eno=int(input("Enter Employee number:"))
                ename = input("Enter Employee name:")
                sal= float(input("Enter Employee Salary:"))
                print("----------------------------")
                #add emp values to list obj
                lst=list()
                lst.append(eno)
                lst.append(ename)
                lst.append(sal)
                #save lst data to the file
                pickle.dump(lst,fp)
                print("Emp Data saved in a File Successfully ")
                print("--------------------------------")
                ch=input("Do you want tp insert another record yes/no")
                if(ch.lower()=="no"):
                    print("Thnx for using this Program")
                    break
            except ValueError:
                  print("Don't enter alnums,strs,and special symbols")
#main program
saveempdata()