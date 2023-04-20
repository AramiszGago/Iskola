print("1. feladat")

for i in range(1):
    a = int(input("Adj meg egy számot:"))
    b = int(input("Adj meg egy számot:"))
    if a > b:
        print("Nagyobbik szám:", a)
    if b > a:
        print("Nagyobbik szám:", b)
    if a == b:
        print("A két szám egyenlő!")

print("2. feladat")

def kodolas(mondat,betu,darab):
    cserel = ""
    db = 0
    for i in mondat:
        if i == betu and db < darab:
            cserel = cserel+str(ord(i))
            db = db+1
        else:
            cserel = cserel+i
    return cserel

szoveg = kodolas("Az almás pite nagyon finom!", "a", 5)
print(szoveg)