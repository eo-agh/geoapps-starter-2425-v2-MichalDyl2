# Importowanie funkcji getcwd
from os import getcwd
import time
import importlib

# Importowanie własnego modułu czas
import czas

# Pobranie i wypisanie bieżącej ścieżki
current_path = getcwd()
print("Aktualny katalog:", current_path)

# Wypisanie wartości aktualnego czasu (pierwsze uruchomienie)
print("Pierwszy czas:", czas.aktualny_czas)

# Opóźnienie 20 sekund
time.sleep(20)

# Wypisanie wartości aktualnego czasu (po 20 sek)
print("Drugi czas:", czas.aktualny_czas)

# Przeładowanie modułu czas
importlib.reload(czas)

# Wypisanie wartości aktualnego czasu po przeładowaniu modułu
print("Trzeci czas:", czas.aktualny_czas)
