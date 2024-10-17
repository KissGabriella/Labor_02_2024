class Teglalap:
    info = "************************"

    def __init__(self, a_oldal, b_oldal):
        self.a_oldal = a_oldal
        self.b_oldal = b_oldal

    def terulet(self):
        return self.a_oldal * self.b_oldal

    def kerulet(self):
        return (self.b_oldal + self.a_oldal) * 2


class Negyzet(Teglalap):
    def __init__(self, a_oldal, b_oldal=0):
        super().__init__(a_oldal, b_oldal)
        self.a_oldal = a_oldal
        self.b_oldal = a_oldal

class Haromszog(Teglalap):
    def __init__(self, a_oldal, b_oldal):
        super().__init__(a_oldal, b_oldal)

    def terulet(self):
        return (self.a_oldal * self.b_oldal) / 2

    def kerulet(self):
        from math  import sqrt
        return self.a_oldal + self.b_oldal + sqrt(self.a_oldal**2 + self.b_oldal**2)


class Kocka(Negyzet):
    def __init__(self, a_oldal):
        super().__init__(a_oldal)
        self.a_oldal = a_oldal

    def felszin(self):
        return self.terulet() * 6




if __name__ == "__main__":
    tegla = Teglalap(4, 5)
    print("Téglalap")
    print(tegla.terulet())
    print(tegla.kerulet())
    print(tegla.info)
    print("Négyzet")
    negy = Negyzet(7)
    print(negy.terulet())
    print(negy.kerulet())
    print(negy.info)
    print("Háromszög")
    harom = Haromszog(3, 4)
    print(harom.terulet())
    print(harom.kerulet())
    print(harom.info)
    print("Kocka")
    koc = Kocka(7)
    print(koc.terulet())
    print(koc.felszin())
    print(koc.info)