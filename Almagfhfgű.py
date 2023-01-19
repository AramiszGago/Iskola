lista = [2, 56, 4, 10, -6, -66, -2, 1, 655]

for i in range(len(lista)-1):
    minindex = i
    for j in range(i+1,len(lista)):
        print(lista)
        if lista[j] < lista[minindex]:
            minindex = j
            print("új minimum találat")
        else:
            print("")
    if i != minindex:
        print("csere")
        lista[i], lista[minindex] = lista[minindex], lista[i]

print(lista)