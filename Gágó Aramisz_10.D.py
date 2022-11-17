for i in range(5):
    print("Adj meg egy számot:")
    a = float(input())
    if a == 0:
        print("A kör opciót választotta:")
        r = float(input())
        print("A kör sugara:", r)
        print("A kör területe:", round((r**2)*3.14))
        print("A kör kerülete:", round(2*r*3.14))
    elif a%2 == 0:
        print("A négyzet opciót választotta:")
        print("A paros szám", a)
        print("A szám négyzete:", a**2)
    else:
        print("Nincs ilyen opcó")