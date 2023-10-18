#Program for generating any 5 random numbers between 1000 to 2000
#RandRangeEx.py
import random as r
print("---------andrange(Value)---------------------")
for i in range(1,11):
    print(r.randrange(0,10000))
print("---------andrange(Start,Stop)----------------")
for i in range(1,11):
    print(r.randrange(1000,10000))
print("---------andrange(Start,Stop,Step)------------")
for i in range(1,11):
    print(r.randrange(1000,10000,5))
print("------------------------------")