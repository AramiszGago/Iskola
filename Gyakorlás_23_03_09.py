#1. feladat
print("1. feladat:")

import math as m

#5x2 -3x -2 = 0

a = 5
b = -3
c = -2

D = m.pow(b,2)-4*a*c
print(D)

#2. feladat
print()
print("2. feladat:")

import math

szam = int(input())
if szam > 0:
    prim = True
    j = 2
    gy = math.sqrt(szam)
    while prim and j <= gy:
        if szam % j == 0:
            prim = False
        else:
            j = j+1
    if prim:
        print("Prím szám")
    else:
        print("Nem prím szám")
else:
    print("Negatív számot vagy 0 adtál meg!")