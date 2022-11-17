print("Adj meg egy számot:")
a = float(input())
sum = 0
for i in range(5):
    print("Adj meg még egy számot:")
    b = float(input())
    sum = sum+b
if sum > a:
    print("Átlag:", sum/5)
else:
    print(sum**2)