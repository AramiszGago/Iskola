lista = [1,9,-6,11,7,12,120,-96,55,42,300,15,-1]

def novekvorend(lista):
    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista)):
                if lista[j] < lista[i]:
                    lista[i], lista[j] = lista[j], lista[i]

def legkisebb(lista):
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i
    return minimum

def legngyobb(lista):
    maximum = lista[0]
    for i in lista:
        if i > maximum:
            maximum = i
    return maximum

novekvorend(lista)
min = legkisebb(lista)
max = legngyobb(lista)
print("Növekvő sorrendbe rendezett lista:", lista)
print("Legkisebb szám:", min)
print("Legnagyobb szám:", max)