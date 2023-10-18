import pickle
def saveempdata():
    nor=int(input("enter how many Employee records u have:"))
    if(nor<=0):
        print("{} Is invalid input".format(nor))
    else:
        with open("emp.info","ab")as fp:
            for i in range(1,nor+1):
                 print("-----------------")
                 print("{} Employee Details".format(i))
                 print("---------------------")
                 eno = int(input("Enter Employee number:"))
                 ename = input("Enter Employee name:")
                 sal = float(input("Enter Employee Salary:"))
                 print("----------------------------")
                 lst=list()
                 #add emp values to list obj
                 lst.append(eno)
                 lst.append(ename)
                 lst.append(sal)
                 #Save lst data to the file
                 pickle.dump(lst,fp)
                 print("Emp Data saved in a File Successfully")
                 print("---------------------")
#Main program
saveempdata()