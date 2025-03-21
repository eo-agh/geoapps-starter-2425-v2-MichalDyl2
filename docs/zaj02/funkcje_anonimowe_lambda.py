# lista ksiazek
ksiazki = [
    {"tytul": "Władca Pierścieni", "autor": "J.R.R. Tolkien", "rok_wydania": 1954},
    {"tytul": "Harry Potter i Kamień Filozoficzny", "autor": "J.K. Rowling", "rok_wydania": 1997},
    {"tytul": "Duma i uprzedzenie", "autor": "Jane Austen", "rok_wydania": 1813},
    {"tytul": "Rok 1984", "autor": "George Orwell", "rok_wydania": 1949},
    {"tytul": "Zbrodnia i kara", "autor": "Fiodor Dostojewski", "rok_wydania": 1866},
    {"tytul": "Mistrz i Małgorzata", "autor": "Michaił Bułhakow", "rok_wydania": 1967},
    {"tytul": "Hobbit", "autor": "J.R.R. Tolkien", "rok_wydania": 1937},
    {"tytul": "Sto lat samotności", "autor": "Gabriel García Márquez", "rok_wydania": 1967},
    {"tytul": "Imię róży", "autor": "Umberto Eco", "rok_wydania": 1980},
    {"tytul": "Solaris", "autor": "Stanisław Lem", "rok_wydania": 1961},
]

# sortowanie wedlug roku wynania (rosnaco)
ksiazki_posortowane = sorted(ksiazki, key=lambda ksiazka: ksiazka["rok_wydania"])

print("\nKsiążki posortowane według roku wydania:")
for ksiazka in ksiazki_posortowane:
    print(f"{ksiazka['rok_wydania']}: {ksiazka['tytul']}")

# filtracja wydanych po 1950 (filtracja po 2000 bez sensu bo nie ma takich ksiazek)
ksiazki_po_2000 = list(filter(lambda ksiazka: ksiazka["rok_wydania"] > 1950, ksiazki))

print("\nKsiążki wydane po 2000 roku:")
for ksiazka in ksiazki_po_2000:
    print(f"{ksiazka['rok_wydania']}: {ksiazka['tytul']}")

# Transformacja listy do listy tytułów
lista_tytulow = list(map(lambda ksiazka: ksiazka["tytul"], ksiazki))

print("\nLista tytulow:")
print(lista_tytulow)
