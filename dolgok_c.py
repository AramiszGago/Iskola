class ember:
    def __init__(self, kor=0, magassag=0, tudas=0, nem=0, csaladnev=0, keresztnev=0, suly=0):
        self.kor = kor
        self.magassag = magassag
        self.tudas = tudas
        self.nem = nem
        self.csaladnev = csaladnev
        self.keresztnev = keresztnev
        self.suly = suly

    def BMI(self):
        return (self.suly/(self.magassag**2))

    def IQ(self):
        return (self.tudas/self.kor)

    def Kepesseg(self):
        print("Tanul")

    def kiir(self):
        print("BMI:", self.BMI, "IQ:", self.IQ, "Képesség:", self.Kepesseg)
