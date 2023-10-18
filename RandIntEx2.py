#Program for generating any 10 random flotaing Point Values between 0.0. 1.0import random as r
import random as r
print("------------------------------")
for i in range(1,11):
    print(r.random())
print("------------------------------")
for i in range(1,11):
    print("%0.2f" %r.random())
print("------------------------------")
for i in range(1,11):
    print(round(r.random(),3))
print("------")