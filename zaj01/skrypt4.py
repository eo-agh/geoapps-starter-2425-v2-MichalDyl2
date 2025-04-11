import json
import re

# Wczytanie pliku JSON
file_path = "teksty.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Połączenie wszystkich tekstów w jeden ciąg znaków
wszystkie_teksty = " ".join([tekst for obj in data["teksty"] for tekst in obj.values()])

# Zamiana na małe litery
wszystkie_teksty = wszystkie_teksty.lower()

# Podział na wyrazy i usunięcie interpunkcji (kropki, przecinki)
wyrazy = re.findall(r'\b\w+\b', wszystkie_teksty)

# Zamiana ostatniego znaku każdego wyrazu na wielką literę
wyrazy = [wyraz[:-1] + wyraz[-1].upper() if len(wyraz) > 1 else wyraz.upper() for wyraz in wyrazy]

# Usunięcie wyrazów bez litery "a" lub "A"
wyrazy = [wyraz for wyraz in wyrazy if "a" in wyraz.lower()]

# Zbiór unikalnych wyrazów
unikalne_wyrazy = set(wyrazy)

# Słownik liczący wystąpienia słów
licznik_wyrazow = {}
for wyraz in wyrazy:
    licznik_wyrazow[wyraz] = licznik_wyrazow.get(wyraz, 0) + 1

# Tworzenie nowego JSON-a z wynikami
wynik = {
    "wszystkie_wyrazy": wyrazy,
    "unikalne_wyrazy": list(unikalne_wyrazy),
    "licznik_wyrazow": licznik_wyrazow
}

# Zapisanie do nowego pliku JSON
output_file_path = "teksty_p.json"

with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(wynik, output_file, indent=4, ensure_ascii=False)

print(f"Plik JSON został zapisany: {output_file_path}")
