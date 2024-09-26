def adatok_bekerese():
    muvelet = input("Milyen műveletet szeretne végrehajtani (+,-,*,/): ")
    while muvelet not in ("+", "-", "*", "/"):
        print("Nem jó műveletet adott meg!\nKérek egy újat")
        muvelet = input("Milyen műveletet szeretne végrehajtani (+,-,*,/): ")


    szam1 = input("Adja meg az elsŐ számot: ")
    while not szam1.isnumeric():
        print("Nem számt adott meg!")
        szam1 = input("Adja meg újra az elsŐ számot: ")
    else:
        szam1 = int(szam1)

    szam2 = input("Adja meg a második számot: ")
    while not szam2.isnumeric():
        print("Nem számt adott meg!")
        szam2 = input("Adja meg újra az elsŐ számot: ")
    else:
        szam2 = int(szam2)
    return szam1, muvelet, szam2



def muveletek_vegrehajtasa(szam1, muvelet, szam2):
    eredmeny = 0
    if muvelet == "+":
        eredmeny = szam1 + szam2
    elif muvelet == "-":
        eredmeny = szam1 - szam2
    elif muvelet == "*":
        eredmeny = szam1 * szam2
    elif muvelet == "/":
        eredmeny = szam1 / szam2
    return eredmeny


def eredmenyek_megjelenitese(szam1, muvelet, szam2, eredmeny):
    print("A művelet végrehajtása:")
    print(str(szam1).rjust(30))
    print(str(szam2).rjust(30))
    print(muvelet, "".rjust(29, "_"), sep="")
    print(str(eredmeny).rjust(30))