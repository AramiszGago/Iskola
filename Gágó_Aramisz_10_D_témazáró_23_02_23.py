def rendezesnov(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return  lista

def rendezescsok(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return  lista

lista = []

while True:
    a = int(input("Adj meg egész számokat:"))
    if a != -1:
        lista.append(a)
    else:
        break

print(lista)
lista2 = rendezesnov(lista)
print(lista2)