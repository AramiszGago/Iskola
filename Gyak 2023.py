lista = []
maximum = 0
minimum = 0

print("Adjon meg 5 számot:")
for i in range(5):
    a = int(input())
    if maximum < a:
        maximum = a
    minimum = lista[0]
    if a in lista:
        if a < minimum:
            minimum = a

print("A maximum:", maximum)
print("A minimum:", minimum)
