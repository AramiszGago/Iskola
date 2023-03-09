szoveg1 = "0123456789"
szoveg2 = "abcdefg"
szoveg3 = ""

if len(szoveg1) > len(szoveg2):
        for i, j in zip(szoveg1[:len(szoveg2)], szoveg2):
            szoveg3 = szoveg3+i+j
        szoveg3 = szoveg3 + szoveg1[len(szoveg2):]

elif len(szoveg1) < len(szoveg2):
        for i, j in zip(szoveg1, szoveg2[:len(szoveg1)]):
            szoveg3 = szoveg3+i+j
        szoveg3 = szoveg3 + szoveg2[len(szoveg1):]

else:
    for i, j in zip(szoveg1, szoveg2):
        szoveg3 = szoveg3+i+j

print(szoveg3)