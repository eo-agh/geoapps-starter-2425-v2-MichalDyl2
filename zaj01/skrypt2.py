# skrypt2.py

import math
import random

# Działania matematyczne
wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie ** 2  # Uniknięcie ogromnej liczby
tekst = str(potega)

wartosc_pi = math.pi
losowa = random.choice([1, 2, 3, 4, 5])

# Łańcuchy znaków
tekst = f"Wartosc: {tekst}"
print(len(tekst))
print(tekst[1:4])
print(tekst.upper())

# Listy
lista = list(tekst)
lista = lista[:8]  # Wyciągnięcie "WARTOSC:"
lista.append([1, 2, 3, 4, 5])

# Usunięcie dwukropka tylko jeśli istnieje
if ":" in lista:
    lista.remove(":")

print(lista)

# Listy składane
lista2 = [1, 2, 3, "banan", 100]
lista3 = [x**2 for x in lista2 if x != "banan"]
lista4 = list(range(2, 17, 2))
print(lista2, lista3, lista4)

# Słowniki
ja = {
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 30,
    "moje_hobby": [
        {"nazwa": "programowanie", "dlaczego": "lubię kodować"},
        {"nazwa": "rower", "dlaczego": "jazda sprawia mi frajdę"}
    ]
}
print(ja["moje_hobby"][0]["nazwa"])
print(ja.keys())
print("adres" in ja)

# Krotki
krotka1 = (1, 2, "3", 4, 2, 5)
print(len(krotka1), krotka1[0])
print(krotka1.count(2))

# Zbiory
X = set("kalarepa")
Y = set("lepy")
print(X & Y)
