homerseklet = [-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-21,-56,-75,80,-77,100,67,22,8,-78,-6]

#

legkisebb = homerseklet[0]
for i in homerseklet:
    if i < legkisebb:
        legkisebb = i

print("Legkisebb hőmérséklet:", legkisebb)

legnagyobb = homerseklet[0]
for i in homerseklet:
    if i > legnagyobb:
        legnagyobb = i

for i,j in enumerate(homerseklet):
    homerseklet[i] = (homerseklet[i]+legnagyobb)
    print("Legmelegebb nap:", i+1, legnagyobb)

