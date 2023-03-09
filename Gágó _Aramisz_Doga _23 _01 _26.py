lista = [10,-2,1,25,22,30,60,-99,-1252,3000,2123,16,12]

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print("Növekvő sorrend:",lista)

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print("Csökkenő sorrend:",lista)

max = lista[0]
for i in range(len(lista)):
    if i > max:
        max = i
print("Maximum:", max)

min = lista[-1]
for i in range(len(lista)):
    if i < min:
        min = i
print("Minimum:", min)