# import lab_05_modul
from lab_05_modul import *


def beleptetes():
    print("Beléptetés")


def regisztracio():
    print("Regisztráció")


#Főprogram
#regisztracio()
#beleptetes()
felhasznalo_neve = felhasznalonev()
print(felhasznalo_neve)
felhasznalo_jelszo = jelszo_bekerese(10)
print(felhasznalo_jelszo)