lista = []
maximum = -1
minimum = 0


print("Adjon meg 5 számot:")
for i in range(5):
    a = int(input())
    lista.append(a)
    if maximum < a:
        maximum = a
    if minimum > a:
        minimum = a

print(lista)
print(maximum, lista.index(maximum))
print(minimum)