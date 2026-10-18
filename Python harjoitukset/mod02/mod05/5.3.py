luku=int(input("5:"))
aluluku = True
if luku < 2:
    aluluku = False
else:
    for i in range(2, luku):
        if luku % i == 0:
            aluluku = False
            break
if aluluku:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")
