osszeg = 0
lista = []
maximum = -1
for i in range(5):
    a = int(input(lista.append))
    lista.append(a)
    osszeg = osszeg+a
    if maximum < a:
        maximum = a

print(lista)
print(osszeg/len(lista))
print(maximum, lista.index(maximum))

for i,j in enumerate(lista):
    lista[i] = (lista[i]+maximum)/len(lista)
    print(i, lista[i])