#terület kerület

print("Add meg az a oldalt:")
a = float(input())

print("Add meg az b oldalt:")
b = float(input())

K = 2*(a+b)
T = a*b

if a == b:
    print("A négyzet területe:", T, "A kerülete:", K)
else:
    print("A téglalap területe:", T, "A kerülete:", K)