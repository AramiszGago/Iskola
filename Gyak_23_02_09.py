def harommal_oszthatok(lista):
    db = 0
    for i in lista:
        if i%3==0:
            db = db+1

    return db

kutya = []

while True:
    a = int(input("Adj meg számokat: "))
    if a >= 0:
        kutya.append(a)
    else:
        break

szamok = harommal_oszthatok(kutya)
print("A listában 3-mal osztható számok száma:", szamok)