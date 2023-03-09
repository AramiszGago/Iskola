while szam > 0:
    szam = float(input("Adj meg egy valós számot:"))
    print("Add meg a mérték egységet (cm, m, km):")
    mertekegyseg = input()
    print("Add meg mire szeretnéd váltani (cm, m, km):")
    atvaltas = input()

    if mertekegyseg == "cm":

        if atvaltas == "cm":
            print(szam, mertekegyseg, "-", szam, atvaltas)
        elif atvaltas == "m":
        M = szam/100
            print(szam, mertekegyseg, "-", M, atvaltas)
        elif atvaltas == "km":
            KM = szam/100000
            print(szam, mertekegyseg, "-", KM, atvaltas)


    if mertekegyseg == "m":

        if atvaltas == "cm":
            CM = szam*100
            print(szam, mertekegyseg, "-", CM, atvaltas)
        elif atvaltas == "m":
            print(szam, mertekegyseg, "-", szam, atvaltas)
        elif atvaltas == "km":
            KM = szam/1000
            print(szam, mertekegyseg, "-", KM, atvaltas)


    if mertekegyseg == "km":

        if atvaltas == "cm":
            CM = szam*100000
            print(szam, mertekegyseg, "-", CM, atvaltas)
        elif atvaltas == "m":
            M = szam*1000
            print(szam, mertekegyseg, "-", M, atvaltas)
        elif atvaltas == "km":
            print(szam, mertekegyseg, "-", szam, atvaltas)