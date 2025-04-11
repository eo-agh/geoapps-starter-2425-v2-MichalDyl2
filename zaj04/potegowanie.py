def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj

# Test:
potega_2 = stworz_funkcje_potegujaca(2)
print(potega_2(4))  # Wynik: 16
