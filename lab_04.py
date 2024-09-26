# Számológép négy alapműveletre

import lab_04_modul

from lab_04_modul import eredmenyek_megjelenitese



# Főprogram
adatok = lab_04_modul.adatok_bekerese()
muvelet_eredmenye = lab_04_modul.muveletek_vegrehajtasa(adatok[0], adatok[1], adatok[2])
eredmenyek_megjelenitese(adatok[0], adatok[1], adatok[2], muvelet_eredmenye)
