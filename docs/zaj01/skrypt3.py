# skrypt3.py

# 1. Pętla for + enumerate()
imiona = ["Anna", "Jan", "Piotr", "Maria"]
for indeks, imie in enumerate(imiona):
    print(f"{indeks}: {imie}")

# 2. Sprawdzanie liczby (dodatnia i parzysta)
liczba = int(input("Podaj liczbę: "))
if liczba > 0 and liczba % 2 == 0:
    print("Liczba jest dodatnia i parzysta.")

# 3. Sprawdzanie liczby (różna od zera)
liczba = int(input("Podaj liczbę: "))
if liczba != 0:
    print("Liczba jest różna od zera.")

# 4. Sprawdzanie dostępności owocu
owoce = ['jabłko', 'banan', 'pomarańcza']
owoc = input("Podaj owoc: ").lower()
if owoc in owoce:
    print("Owoc jest dostępny.")

# 5. Pętla while - sumowanie liczb do 100
suma = 0
while suma <= 100:
    liczba = int(input("Podaj liczbę do dodania: "))
    suma += liczba
print(f"Suma przekroczyła 100! Wynosi: {suma}")
