import math
a = int(input())
b = int(input())

muvelet = input()

eredmeny = -1

if muvelet == "+":
    eredmeny = a+b
elif muvelet == "-":
    eredmeny = a-b
elif muvelet == "/":
    eredmeny = a/b
elif muvelet == "*":
    eredmeny = a*b
elif muvelet == "**":
    eredmeny = a**b
elif muvelet == "gyök":
    eredmeny = math.sqrt(a), math.sqrt(b)
    # vagy a**(0.5), b**(0.5)
else:
    print("Nincs ilyen művelet")

print(eredmeny)