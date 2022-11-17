homerseklet = float(input("Add meg a hőmérsékletet: "))
print("Add meg miről szeretnéd, C = Celsius, F = Farenheit, K = Kelvin: ")
kmertekegyseg = input()
print("Add meg mire szeretnéd, C = Celsius, F = Farenheit, K = Kelvin: ")
mire = input()

if kmertekegyseg == "C":

    if mire == "C":
        print("A hőmérséklet Celsiusban:", homerseklet)
    elif mire == "F":
        F = homerseklet*1.8+32
        print("A hőmérséklet Farenheitben:", F)
    elif mire == "K":
        K = homerseklet + 273.15
        print("A hőmérséklet Kelvinben:", K)


if kmertekegyseg == "F":

    if mire == "C":
        C = (homerseklet-32)/1.8
        print("A hőmérséklet Celsiusban:", C)
    elif mire == "F":
        print("A hőmérséklet Farenheitben:", homerseklet)
    elif mire == "K":
        C = (homerseklet-32)/1.8
        K = C + 273.15
        print("A hőmérséklet Kelvinben:", K)


if kmertekegyseg == "K":

    if mire == "C":
        C = homerseklet-273.15
        print("A hőmérséklet Celsiusban:", C)
    elif mire == "F":
        C = homerseklet-273.15
        F = C*1.8+32
        print("A hőmérséklet Farenheitben:", F)
    elif mire == "K":
        print("A hőmérséklet Kelvinben:", homerseklet)