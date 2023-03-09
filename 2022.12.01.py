#maximum keresés (minimum keresés a kacsacsőr fordítva áll, elnevezés pl.: minElem):
t = [5, 3, 6, 2, 1]

maxElem = t[0]
for i in t:
    if i > maxElem:
        maxElem = i

print(maxElem)


maxElem = t[0]
maxhely = t[0]
for i in range(1, len(t)):
    if t[i] > maxElem:
        maxElem = t[i]
        maxhely = i

print(maxElem, maxhely)


#Öszegzés: (szorzás, osztás, és kivonás, ugyanúgy működik):

p = [3, 8, 2, 4, 5, 1, 6]

osszeg = 0
for num in p:
    osszeg = osszeg+num

print("Összeg:", osszeg)


#Megszámlálás (pozitív, negatív, stb.):

u = [3, -8, 2, 4, 5, 11, 6]

count = 0
for num in u:
    if num < 0:
        count = count+1

print("Negatív számok:", count)


#Eldöntés (in, not in)(szöveges is lehet):

k = [3, 8, 2, 4, 5, 1, 6]

n = len(k)
ker = 5
i = 0
while i < n and k[i] != ker:
    i = i+1
if i < n:
    print("Van ilyen:", ker)
else:
    print("Nincs ilyen elem:", ker)


#Kiválasztás (Keresés, kisebb kiegészítéssel):

k = [3, 8, 2, 4, 5, 1, 6]

n = len(k)
ker = 5

i = 0
while i < n and k[i] != ker:
    i = i+1

print("Hányadik helyen van:", i+1)


#Kiválogatás (nagyokat, kicsiket, stb.):

a = [3, 8, 2, 4, 5, 1, 6, 7, 9, 23, 12]
b = []

for elem in a:
    if elem < 5:
        b.append(elem)

print(b)


#Szétválogatás:

a = [3, 8, 2, 4, 5, 1, 6, 7, 9, 23, 12]
b = []
c = []

for elem in a:
    if elem < 5:
        b.append(elem)
    else:
        c.append(elem)

print(b)
print(c)