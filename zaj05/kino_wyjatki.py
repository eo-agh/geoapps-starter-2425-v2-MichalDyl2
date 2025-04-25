class BrakMiejscError(Exception):
    pass

class MiejsceZajeteError(Exception):
    pass

class PodwojnaRezerwacjaError(Exception):
    pass

class Kino:
    def __init__(self, miejsca):
        self.miejsca = miejsca  # np. {'A1': None, 'A2': None}
        self.uzytkownicy = {}

    def rezerwuj(self, miejsce, imie_nazwisko):
        if all(v is not None for v in self.miejsca.values()):
            raise BrakMiejscError("Brak wolnych miejsc.")

        if miejsce not in self.miejsca:
            raise ValueError("Nie ma takiego miejsca.")

        if self.miejsca[miejsce] is not None:
            raise MiejsceZajeteError("To miejsce jest już zajęte.")

        if imie_nazwisko in self.uzytkownicy.values():
            raise PodwojnaRezerwacjaError("Użytkownik już zarezerwował miejsce.")

        self.miejsca[miejsce] = imie_nazwisko
        self.uzytkownicy[miejsce] = imie_nazwisko
        print(f"✅ Zarezerwowano miejsce {miejsce} dla {imie_nazwisko}")

    def anuluj(self, miejsce, imie_nazwisko):
        if self.miejsca.get(miejsce) == imie_nazwisko:
            self.miejsca[miejsce] = None
            del self.uzytkownicy[miejsce]
            print(f"❌ Rezerwacja miejsca {miejsce} została anulowana.")
        else:
            raise ValueError("Nie można anulować – dane się nie zgadzają.")

# Test
kino = Kino({'A1': None, 'A2': None})

try:
    kino.rezerwuj("A1", "Jan Kowalski")
    kino.rezerwuj("A2", "Jan Kowalski")  # próba podwójnej rezerwacji
except Exception as e:
    print("❗ Błąd:", e)

try:
    kino.anuluj("A1", "Jan Kowalski")
except Exception as e:
    print("❗ Błąd:", e)
