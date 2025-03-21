# skrypt5.py

# 1. Rozpakowywanie krotek i list
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print(rok, jezyk, wersja)

oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print(pierwsza, srodek, ostatnia)

info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, _, _, zawod = info
print(imie, nazwisko, zawod)

dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok, (jezyk, wersja, (opis, _)) = dane
print(rok, jezyk, wersja, opis)

# 2. Współdzielone referencje
a = b = [1, 2, 3]
b[0] = 'zmieniono'
print(a, b)  # Lista a i b zmieniona, bo wskazują na ten sam obiekt

# 3. Kopiowanie listy
c = list(a)  # Można też użyć: a[:]
c[0] = 'nowa wartość'
print(a, b, c)  # a i b nie zmieniły się, bo c to nowa lista

# 4. Przypisanie do zmiennych niemutowalnych (integer)
x = y = 10
y = y + 1
print(x, y)  # x nie zmienia się, bo liczby są niemutowalne

# 5. Przypisania rozszerzone
K = [1, 2]
L = K
K = K + [3, 4]  # Tworzy nową listę, L nie zmienia się

M = [1, 2]
N = M
M += [3, 4]  # Modyfikuje istniejącą listę, więc N też się zmienia

print(K, L)  # L zostaje bez zmian
print(M, N)  # N się zmienia razem z M
