#By using open()
fp=open("stdu1.data","w")
print("File created and opened in write mode")
print("Type of fp=",type(fp))
print("Is file closed before close=",fp.closed)

print("Is file closed After close=",fp.close)
print("File Name:",fp.name)
print("File Mode:",fp.mode)
print("Is File Readable:",fp.readable())
print("Is File writable:",fp.writable())
print("Is file closed After close=",fp.closed)