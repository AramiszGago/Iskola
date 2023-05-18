#1. feladat
i = int(input("Adj meg egy egész számot:"))
if i % 2 == 0:
    print("A szám páros!")
else:
    print("A szám páratlan!")

#2. feladat
def email(nev, osztaly):
    nev = nev.lower()
    osztaly = osztaly.lower()

    ev = 2023-(int(osztaly.split(".")[0])-8)
    csoport = osztaly.split(".")[1]


    ekezet = ["á", "é", "í", "ő", "ű", "ó", "ú"]
    mentes = ["a", "e", "i", "ö", "ü", "o", "u"]

    for i,j in zip(ekezet,mentes):
        nev = nev.replace(i,j)

    nev = nev.replace(" ",".")

    email = nev+".tech"+str(ev)+csoport+"@bolyaimovar.com"

    return email

em = email("Gágó Aramisz", "10.D")
print(em)


#3. feladat
#a. rész
import copy

hegyek = []
dict = {}
with open("hegyekMo.txt", "r", encoding="utf-8") as file:
    i = 0
    for sor in file:
        if i != 0:
            dict["Hegycsúcs neve"] = sor.strip().split(";")[0]
            dict["Hegység"] = sor.strip().split(";")[1]
            dict["Magasság"] = int(sor.strip().split(";")[2])
            hegyek.append(copy.deepcopy(dict))

        else:
            i = i+1

minimum = hegyek[0]["Magasság"]
hegy = hegyek[0]["Hegycsúcs neve"]
atl = 0
borzsony = []
for i in hegyek:
    atl = i["Magasság"]+atl
    if i["Magasság"] < minimum:
        minimum = i["Magasság"]
        hegy = i["Hegycsúcs neve"]


    if i["Hegység"] == "Börzsöny":
        borzsony.append(i)

#b. rész
print(str(minimum)+" "+hegy)

#c. rész
atl = round(atl/len(hegyek),2)
print(atl)

#d. rész
with open("borzsony.txt", "w", encoding="utf-8") as file:
    for i in borzsony:
        file.write(i["Hegycsúcs neve"]+" "+str(i["Magasság"])+"\n")