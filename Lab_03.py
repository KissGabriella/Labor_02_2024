""" Jövedelemszámítás bruttó és kor alapján

print("Jövedelemszámítás\n")
brutto = int(input("Kérem a bruttó jövedelmét: "))
kor = int(input("Mi az életkora: "))

if kor < 25:
        if brutto < 599790:
            szja = 0
        else:
            szja = (brutto - 599790) * 0.15
else:
    szja = brutto * 0.15
nyuddij = brutto * 0.1
tb = brutto * 0.07
munkanelkuli= brutto * 0.015
netto = brutto - szja -nyuddij - tb - munkanelkuli

print("Jövedelem".center(50))
print("")
print("Bruttó jövedelem:".ljust(25, "_"), str(brutto).rjust(25, "_"), " Ft", sep="")
print("SZJA:".ljust(25, "_"), str(int(szja)).rjust(25, "_"), " Ft", sep="")
print("Nyugdíj:".ljust(25, "_"), str(int(nyuddij)).rjust(25, "_"), " Ft", sep="")
print("TB:".ljust(25, "_"), str(int(tb)).rjust(25, "_"), " Ft", sep="")
print("Munkanélküli J.:".ljust(25, "_"), str(int(munkanelkuli)).rjust(25, "_"), " Ft", sep="")
print("")
print("Nettó:".ljust(25, "_"), str(int(netto)).rjust(25, "_"), " Ft", sep="")
"""

# Számológép négy alapműveletre
print("Számológép")
muvelet = input("Milyen műveletet szeretne végrehajtani (+,-,*,/): ")
if muvelet not in ("+", "-", "*", "/"):
    print("Nem jó műveletet adott meg!")
    exit()
else:
    szam1 = int(input("Adja meg az elsŐ számot: "))
    szam2 = int(input("Adja meg a második számot: "))

    if muvelet == "+":
        eredmeny = szam1 + szam2
    elif muvelet == "-":
        eredmeny = szam1 - szam2
    elif muvelet == "*":
        eredmeny = szam1 * szam2
    else:
        if szam2 == 0:
            print("Nullával nem lehet osztani!")
            exit()
        else:
            eredmeny = szam1 / szam2

print("A művelet: ", str(szam1), muvelet, str(szam2), "=", eredmeny)