import random as r
ads="abc01234d$efghiABCDEF#GH56789!IJKLMjklm&no@pqrstuvwx*yzNOPQR[STUVWXYZ"
print("--------------------------")
for i in range(1,6):
    print(r.choice(ads)+r.choice(ads)+r.choice(ads)+r.choice(ads)+r.choice(ads)+r.choice(ads))
print("--------------------------")
