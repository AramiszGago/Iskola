konyvek = {}
while True:
    szerzo = input()

    if szerzo == "":
        break
    else:
        cim = input()
        konyvek[szerzo] = cim

for i,j in konyvek.items():
    print(i," : ",j)

#for i in konyvek.keys():
    #print(i," : ",konyvek[i])