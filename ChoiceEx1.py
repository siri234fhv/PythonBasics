import random as r
la="abcdefghijklmnopqrstwuvxyz"
ua="ABCDEFGHIJKLMNOPQRSTWUVXYZ"
d="0123456789"
print("-------------------------")
for i in range(1,6):
    print(r.choice(ua)+r.choice(la)+r.choice(d)+r.choice(ua)+r.choic(d))