szoveg = input("Adj meg egy szöveget:")
db = 0
szamok = "0123456789"
for i in szoveg:
    if i in szamok:
        db = db+1
        print(i)

print("Ennyi szám van a szövegben:", db)