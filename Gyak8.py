lista1 = [-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-21,-56,-75,80,-77,100,67,22,8,-78,-6]

elem = lista1[0]
for i in lista1:
    if i:
        elem = elem+1

print("Elem számok:",elem)

count = 0
for i in lista1:
    if i < 0:
        count = count+1
print("Van negatív szám")


paros = 0
for i in lista1:
    if i % 2 == 0:
        paros = paros+1

print("Páros számok:", paros)


legnagyobb = lista1[0]
for i in lista1:
    if i > legnagyobb:
        legnagyobb = i

print("Legnagyobb szám:", legnagyobb)


tizzel = 0
for i in lista1:
    if i%10 == 0:
        tizzel = tizzel + 1

print("Tizzel osztható:", tizzel)


i = 0
while i < elem and lista1[i] % 29 != 0:
    i = i+1

print("Helye:", i, "Szám:", lista1[i])

Logikai = True
i = 0
while i < elem and lista1[i] %2 ==0:
    i = i+1

if i < elem:
    Logikai = False

print("Minden szám páros?", Logikai)


atl = 0
osszeg = 0
for i in lista1:
    osszeg = osszeg+i

atl = round(osszeg/atl, 2)

