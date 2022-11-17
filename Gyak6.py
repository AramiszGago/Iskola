# a = range(5)
# a = range(1,5,1), range(1(mettől), 5(meddig), 1(hányasával))

#a = 6
#for i in range(6):
#   print(i)

#for i in range(6):
    # i = 0-tól, amíg i < 6, csináld és növeld i+1
    #print(i)


#a = 5
#b = 7
#while a < b:

    #print(a)
    #a = a+1

#print("vége")

#a = 10
#b = 0
#while b == 0: # !=: nem egyelő, ==: egyelő, <=: pozitív számok, >=: negatív számok
    #b = float(input())

#print(a/b)


#nev = "Martin"

#for i in nev:
    #print(i)

#nev = "Martin"
#x = False

#for i in nev:
    #if i == "x":
        #x = True

#if x:
    #print("Special")

jomegoldas = "abcde"
megoldas = "abc"
a = False
b = False
c = False
d = False
e = False


for i in jomegoldas:
    for j in megoldas:

        if j == i:
            if i == "a":
                a = True
            elif i == "b":
                b = True
            elif i == "c":
                c = True
            elif i == "d":
                d = True
            elif i == "e":
                e = True
if a and b and c and d and e:
    print("Good!")
else:
    print("Bad!")
