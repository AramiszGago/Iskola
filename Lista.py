lista = [1,2,3,4,5,6,7]
lista[0] = 100
print(lista[0])

for i,j in enumerate(lista):
    print(i,j)
    lista[i] = lista[i]+100
    print(i,lista[i])