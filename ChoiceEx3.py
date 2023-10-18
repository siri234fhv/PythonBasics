import random as r
d="0123456789"
a="abcdefghiABCDEFGHIJKLMjklmnopqrstuvwxyzNOPQRSTUVWXYZ"
print("-----------------------------")
for i in range(1,6):
    print(r.choice(a)+r.choice(d)+r.choice(d)+r.choice(a)+r.choice(a)+r.choice(d))