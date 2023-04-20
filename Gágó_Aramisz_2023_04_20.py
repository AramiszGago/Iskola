import copy

def teljes_hossz(Zenelista):
    osszeg = 0
    for i in Zenelista:
        osszeg = osszeg + i["hossz"]

    perc = int(osszeg/60)
    mp = int(60*(osszeg/60-perc))
    with open("02_hossz.txt", "w", encoding="utf-8") as file:
        file.write("A lejátszási lista hossza: "+str(perc)+" perc "+str(mp)+" másodperc")

def leggyakoribb_mufaj(Zenelista):
    mufajok = []
    max = 0
    leggyakoribb = ""
    for i in Zenelista:
        if not i["mufaj"] in mufajok:
            mufajok.append(i["mufaj"])

    for i in mufajok:
        db = 0
        for j in Zenelista:
            if j["mufaj"] == i:
                db = db+1
        if db > max:
            max = db
            leggyakoribb = i

    with open("04_kedvenc_mufaj.txt", "w", encoding="utf-8") as file:
        file.write(leggyakoribb.upper())

Zenelista = []
dic = {}

with open("playlist.csv", "r", encoding="utf-8") as file:
    for sor in file:
        dic["eloado"] = sor.strip(";").split(";")[0]
        dic["cim"] = sor.strip().split(";")[1]
        dic["mufaj"] = sor.strip().split(";")[2]
        dic["hossz"] = int(sor.strip().split(";")[3])
        Zenelista.append(copy.deepcopy(dic))

print(Zenelista)
teljes_hossz(Zenelista)
leggyakoribb_mufaj(Zenelista)