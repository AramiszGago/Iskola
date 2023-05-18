class Teglalap:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def ter(self):
        return self.a*self.b

    def ker(self):
        return 2*(self.a+self.b)

    def kiir(self):
        print("Kerület:", self.ker(), "Terület:", self.ter())

    def atlo(self):
        return self.a*self.a+self.b*self.b

    def sugar(self):
        return self.atlo()/2


class Negyzet(Teglalap):
    def __init__(self, a=0):
        self.a = a
        self.b = a