#a
def csöksor(lista):
    for i in range(0,len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

lista = []

with open("egysoros.txt", "r", encoding="utf-8") as file:
    for sor in file:
        lista = sor.strip().split(";")

for i in range(len(lista)):
    lista[i] = int(lista[i])

csöksor(lista)
print("Eredeti lista:", sor)
print("Csökkenő sorrendbe rendezett lista:", lista)

#b
csöksor(lista)
st = ""
for i in lista:
    st = st+str(i)+";"

with open("egysoros_eredmény.txt", "w", encoding="utf-8") as file:
    file.write("Csökkenő sorrendbe rendezett lista:"+st+"\n")

#c
lista2 = []

with open("többsoros.txt", "r", encoding="utf-8") as file:
    for sor in file:
        lista2.append(sor.strip().split(";"))

print("Többsoros lista:")
for i in range(len(lista2)):
    for j in range(len(lista2)):
        lista2[i][j] = int(lista2[i][j])

csöksor(lista2)
egy = ""
for i in lista:
    egy = egy+str(i)+";"

with open("többsoros_eredmény.txt", "w") as file:
    for i in lista2:
        sor = ""
        for j in i:
            sor = sor+str(j)+""
        file.write(sor+"\n")