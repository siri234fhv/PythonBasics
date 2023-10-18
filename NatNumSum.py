#program for Finding Sum of First N Natural Numbers
#NatNumsSumEx1.py
n=int(input("Enter How Many Natural Nums Sum u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Sum of First {} Natural Numbers ".format(n))
    print("-" * 50)
    p=0 # Additive Identity
    d=1
    while(d<=n):
        print("\t{}".format(d))
        p=p+d
        d=d+1
    else:
        print("-"*50)
        print("sum={}".format(p))
        print("-" * 50)

