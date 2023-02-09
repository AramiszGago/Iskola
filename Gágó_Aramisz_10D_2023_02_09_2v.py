lista = [1,9,-6,11,7,12,120,-96,55,42,300,15,-1]

def novekvorend(lista):
    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista)):
            if lista == "novekvo":
                if lista[j] < lista[i+1]:
                    lista[i], lista[j] = lista[j], lista[i]
            else:
                if lista[j] < lista[i]:
                    lista[i], lista[j] = lista[j], lista[i]

novekvorend(lista)
print("Növekvő sorrendbe rendezett lista:", lista)