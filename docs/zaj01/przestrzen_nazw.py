# przestrzen_nazw.py

x = 10  # Zmienna globalna

def funkcja():
    x = 5  # Zmienna lokalna
    print(f'Wartość x wewnątrz funkcji: {x}')

funkcja()
print(f'Wartość x na poziomie globalnym: {x}')

