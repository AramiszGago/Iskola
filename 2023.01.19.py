napok=[]

sum = 0

for i in range(30):
    a = float(input())
    napok.append(a)
    sum = sum+a

min = napok[0]
max = napok[0]
mind = 0
count = 0
for n,i in enumerate(napok):
    sum = sum+i
    if i < min:
        mim = i;
    if i > max:
        max_index = i
        mind = n
    if i < 0:
    counter = counter+1

atl = sum/len(napok)

