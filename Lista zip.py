nev = ["Julcsi", "Peti", "Niki", "Csilla", "Jani", "Kevin"]

szul_ev = [2002, 1987, 2006, 1999, 2022, 1987]

kor = []

for i, j in zip(nev, szul_ev):
    print(i, "-", j)
    print(i, "-", 2022-j)
    kor.append(2022-j)
    print(kor)


legoregebb = kor[0]
for i in kor:
    if i > legoregebb:
        legoregebb = i

print(legoregebb)


legfiatalabb = kor[0]
for i in kor:
    if i < legfiatalabb:
        legfiatalabb = i

print(legfiatalabb)

oregek = []
fiatalok = []

for i, j in zip(nev, kor):
    if j == legoregebb:
        print(i, j)
        oregek.append(i)

for i, j in zip(nev, kor):
    if j == legfiatalabb:
        print(i, j)
        fiatalok.append(i)

print(oregek)
print(fiatalok)
