class MojPlik:
    def __init__(self, nazwa_pliku, tryb):
        self.nazwa_pliku = nazwa_pliku
        self.tryb = tryb

    def __enter__(self):
        print("🔓 Otwieram plik...")
        self.plik = open(self.nazwa_pliku, self.tryb)
        return self.plik

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"❗ Wystąpił błąd: {exc_value}")
        print("🔒 Zamykam plik...")
        self.plik.close()

# Użycie menadżera kontekstu:
with MojPlik("test.txt", "w") as f:
    f.write("To linijka zapisana przez nasz własny menadżer kontekstu!")
    # Możesz też spróbować podnieść błąd, żeby zobaczyć działanie exit
    # raise ValueError("Coś poszło nie tak!")  
