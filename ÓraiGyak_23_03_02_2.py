konyvek = {}
while True:
    cimek = {}
    szerzo = input("Addj meg egy szerzőt:")

    if szerzo == "":
        break
    else:
        while True:
            cim = input("Addj meg egy könyv címét:")
            if cim == "":
                break
            else:
                kiadas = int(input("Add meg a könyv kiadási dátumát:"))
                mufaj = input("Add meg a műfaját:")
                leiras = input("Röviden ird le a mű tartalmát:")

                cimek[cim] = {"Kiadási év:":kiadas, "Műfaj:":mufaj, "Tartalma:":leiras}
            konyvek[szerzo] = cimek

for szerzo,cimek in konyvek.items():
    print("Szerző:",szerzo,)
    for cim,adatok in cimek.items():
        print("\t könyv:", cim,)
        for Adat_kulcs, Adat_érték in adatok.items():
            print("\t\t", Adat_kulcs, Adat_érték)

#for i,j in konyvek.items():
    #print(i," : ",j)

#for i in konyvek.keys():
    #print(i," : ",konyvek[i])