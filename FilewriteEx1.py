sno=300
sname="Travis"
marks=66.54
 #write sno,sname,marks in file---write operation
with open("student.data","a") as fp:
     #save sno value in file
      fp.write(str(sno)+"\t")
#save sname value in file
      fp.write(sname+"\t")
#save marks value in file
      fp.write(str(marks)+"\t")
      fp.write("\n")
      print("Data written to the file")