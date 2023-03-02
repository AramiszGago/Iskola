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

                cimek[cim] = {"Kiadási év":kiadas, "Műfaj":mufaj, "Tartalma":leiras}
            konyvek[szerzo] = cimek

for i,j in konyvek.items():
    print(i," : ",j)

#for i in konyvek.keys():
    #print(i," : ",konyvek[i])