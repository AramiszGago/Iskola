def rendez(szamok):
    for i in range(0,len(szamok)-1):
        for j in range(i,len(szamok)):
            if szamok[i] > szamok[j]:
                szamok[i], szamok[j] = szamok[j], szamok[i]

szamok = []
minimum = []
with open("lista.txt", "r", encoding="utf-8") as file:
    for sor in file:
        szamok = sor.split(";")

for i in range(len(szamok)):
    szamok[i] = int(szamok[i])

rendez(szamok)
print("Rendezett lista:", szamok)
print("Legkisebb szám:", szamok[0])
print("Legnagyobb szám:", szamok[len(szamok)-1])

#új fájlba kiírás
rendez(szamok)
st = ""
for i in szamok:
    st = st+str(i)+""

with open("ujlista.txt", "w", encoding="utf-8") as file:
        file.write("Rendezett lista:"+st+"\n")
        file.write("Legkisebb szám:"+str(szamok[0])+"\n")
        file.write("Legnagyobb szám:"+str(szamok[len(szamok)-1]))