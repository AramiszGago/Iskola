def legkisebb(lista):
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i
    return minimum


szamok = []

while True:
    a = int(input("Adj meg számokat: "))
    if a != 0:
        szamok.append(a)
    else:
        break

min = legkisebb(szamok)
print("Legkisebb szám:", min)