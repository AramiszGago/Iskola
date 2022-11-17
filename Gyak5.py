#  F to C = (F-32)/1.8
#  C to F = C*1.8+32

homerseklet = float(input("Add meg a hőmérsékletet: "))
print("Add meg a mértékegységet. C = Celsius, F = Farenheit, K = Kelvin.")
mertekegyseg = input()

if mertekegyseg == "C":
    #Alap hőmérseklet celsius, ezt már nem kell számolni
    #F-et kell számolni, C to F = C*1.8+32
    #Külön változó
    #Kiírni az összes egységben
    F = homerseklet*1.8+32
    K = homerseklet+273.15
    print("A hőmérséklet Celsiusban:", homerseklet)
    print("A hőmérséklet Farenheitben:", F)
    print("A hőmérséklet Kelvinben:", K)

elif mertekegyseg == "F":
    C = (homerseklet-32)/1.8
    K = C+273.15
    print("A hőmérséklet Farenheitben:", homerseklet)
    print("A hőmérséklet Celsiusban:", C)
    print("A hőmérséklet Kelvinben:", K)
elif mertekegyseg == "K":
    C = homerseklet-273.15
    F = C*1.8+32
    print("A hőmérséklet Kelvinben:", homerseklet)
    print("A hőmérséklet Celsiusban:", C)
    print("A hőmérséklet Farenheitben:", F)