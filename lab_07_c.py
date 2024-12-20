class Jelszo:
    felhasznalo_jelszava = "nincs"

    def __init__(self, felhasznalo_jelszava = "valamiJelszo123"):
        self.felhasznalo_jelszava = felhasznalo_jelszava

    def jelszo_vizsgalata(self, hosszusag):
        jelszo_ok = True
        def hossz(_jelszo, min_hossz):
            ok = True
            if len(_jelszo) < min_hossz :
                ok = False
            return ok

        def szamjegyek(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isnumeric():
                    ok = True
                    break
            return ok


        def kisbetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.islower():
                    ok = True
                    break
            return ok

        def nagybetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isupper():
                    ok = True
                    break
            return ok

        jelszo = self.felhasznalo_jelszava
        if not hossz(jelszo, hosszusag) or not szamjegyek(jelszo) or not kisbetu(jelszo) or not nagybetu(jelszo) or " " in jelszo:
            jelszo_ok = False
        return jelszo_ok

    def jelszo_generalasa(self, hossz=8, kisbetu = True, nagybetu = True, szam = True):
        import string
        import  random
        jelszo = ""
        karaktersor = ""
        if kisbetu:
            karaktersor = string.ascii_lowercase
        if nagybetu:
            karaktersor = karaktersor + string.ascii_uppercase
        if szam:
            karaktersor = karaktersor + string.digits
        for _ in range(hossz):
            jelszo = jelszo + karaktersor[random.randint(0, len(karaktersor)-1)]
            self.felhasznalo_jelszava = jelszo

    def jelszo_ellenorzese(self):
        ok = False
        proba = 0
        while True:
            jelszo2 = input("Ismételje meg a jelszót: ")
            if self.felhasznalo_jelszava == jelszo2:
                ok = True
                break
            else:
                proba += 1
                print("Nem megfelelő a jelszó!")
                if proba == 3:
                    break
        return ok


class Felhasznalo(Jelszo):
    felhasznalo_neve = "Valaki@valami.hu"

    def __init__(self, felhasznalo_jelszava = "ÚjJelszó2"):
        super().__init__(felhasznalo_jelszava)

    def felhasznalonev(self):
        _felhasznalo_neve = input("Kérem a felhasználó nevet (email): ")
        while " " in _felhasznalo_neve or "@" not in _felhasznalo_neve or "." not in _felhasznalo_neve :
            print("Érvénytelen email formátum!")
            if " " in _felhasznalo_neve:
                print("Szóközhasználat az email-ben!")
            if "@" not in _felhasznalo_neve:
                print("Nincs @ az email-ben!")
            if "."not in _felhasznalo_neve:
                print("Nincsen . az email-ben!")
            _felhasznalo_neve = input("Kérem a felhasználó nevet (email): ")
        self.felhasznalo_neve = _felhasznalo_neve

    def rogzites(self):
        with open('dolgozok.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(self.felhasznalo_neve + ";" + self.felhasznalo_jelszava + "\n")

    def tarolas(self):
        import sqlite3
        kapcsolat = sqlite3.connect("dolgozok.db")
        ab = kapcsolat.cursor()
        ab.execute('CREATE TABLE IF NOT EXISTS dolgozok(nev TEXT, jelszo TEXT)')
        nev = self.felhasznalo_neve
        jelszo = self.felhasznalo_jelszava
        ab.execute('INSERT INTO dolgozok (nev, jelszo) VALUES (?, ?)', (nev, jelszo))
        kapcsolat.commit()
        kapcsolat.close()

    def felh_es_jelszo_ell(self):
        import sqlite3
        belepes = False
        kapcsolat = sqlite3.connect("dolgozok.db")
        ab = kapcsolat.cursor()
        nev = self.felhasznalo_neve
        ab.execute('SELECT * FROM dolgozok WHERE nev= ?', (nev,))
        rekord = ab.fetchone()
        if rekord is None:
            belepes =False
        else:
            jelszo = rekord[1]
            if jelszo == self.felhasznalo_jelszava:
                belepes = True
        kapcsolat.close()
        return belepes
