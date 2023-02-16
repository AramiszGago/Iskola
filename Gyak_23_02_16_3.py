#a
a = "almáspite"

print(a)
n = a[8]
o = 0
while o < 9:
    print(a[8-o], end=" ")
    o = o+1

print()

#b
b = "géza kék azég"

print(b)
n = b[12]
k = 0
while k < 13:
    print(b[12-k], end=" ")
    k = k+1

print()

#c
mondat = "Szeretem az almáspitét "
szó = ""

print(mondat)
for i in mondat:
    if i == " ":
        print(szó)
        szó = ""
    else:
        szó = szó+i

#Másik megoldás
#for i in c.split(" "):
    #print(i)