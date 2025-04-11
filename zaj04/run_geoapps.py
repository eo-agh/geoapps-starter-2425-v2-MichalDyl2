from geoapps.zajecia01.dodawanie import dodaj
from geoapps.zajecia04.zasiegi import licznik_nonlocal

print("Dodawanie 3 + 4 =", dodaj(3, 4))

licznik = licznik_nonlocal()
print("Licznik:", licznik())
print("Licznik:", licznik())
