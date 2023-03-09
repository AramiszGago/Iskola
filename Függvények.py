lista1 = [1,23,-4325,546-345,234,324,-3255432,-3455]
lista2 = [23,-3214,21,5424,435,112]
lista3 = [4325,345,-35,43543,-435,345,43587]
lista4 = [lista1,lista2,lista3]
minimumok = []

def minKeres(lista):
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i
    print(minimum)
    return minimum

for i in lista4:
    minimumok.append(minKeres(i))