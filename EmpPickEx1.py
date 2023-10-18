import pickle
def saveempdata():
    with open("emp.pick","ab") as fp: #ab means append,b is binary
        #read emp data from Keyboard
        print("-----------------------------")
        eno=int(input("Enter Employee number:"))
        ename= input("Enter Employee name:")
        sal=float(input("Enter Employee Salary:"))
        print("---------------------------------")
        #add emp values to list obj
        lst=list()
        lst.append(eno)
        lst.append(ename)
        lst.append(sal)
        #save lst data to the file
        pickle.dump(lst,fp)
        print("Emp Data saved in a file Successfully")
#main memory
saveempdata() #Function call