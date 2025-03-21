#funkcja
def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):  
    wartosc = cena * ilosc
    tekst = f"Zamówienie: {nazwa_produktu}, Ilość: {ilosc}, Łączna cena: {wartosc:.2f} zł"
    return tekst, wartosc  #zwracamy zmienne zeby sobie zobaczyc

#lista pusta  
zamowienia = []

#trzy zamowienia
zamowienia.append(zamowienie_produktu("Laptop", cena=3500, ilosc=2))
zamowienia.append(zamowienie_produktu("Myszka", cena=99.99, ilosc=3))
zamowienia.append(zamowienie_produktu("Klawiatura", cena=199.99))  # ilość domyślnie = 1

#Iteracja, wyswietlenie zamowien
print("\nLista zamówień:")
for tekst, wartosc in zamowienia:
    print(tekst)

#Calkowity koszt
suma_zamowien = sum( wartosc for _, wartosc in zamowienia )
print(f"\nŁączna wartość zamówień: {suma_zamowien:.2f} zł")
