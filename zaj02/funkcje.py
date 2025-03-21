import random
def generuj_losowa(seed=None):
    # Ustawienie ziarna (seed) generatora liczb losowych
    if seed is not None:
        random.seed(seed)
    # Generowanie losowej liczby z zakresu od 0 do 100
    return random.randint(0, 100)

liczba = generuj_losowa(seed=42)
print(f"Wygenerowana liczba: {liczba}")