def zmien_wartosc(arg):
    if isinstance(arg, list): #jesli lista
        print(f"Przed zmianą (lista): {arg}")
        arg[0] = 'kalafior'
        print(f"Po zmianie (lista): {arg}")
    elif isinstance(arg, int):  #jesli liczba calkowita
        print(f"Przed zmianą (int): {arg}")
        arg = 65482652
        print(f"Po zmianie (int): {arg} (tylko wewnątrz funkcji!)")
    else:
        print("Nieobsługiwany typ danych!")

#test lista
moja_lista = [1, 2, 3]
zmien_wartosc(moja_lista)  
print(f"Po wywołaniu funkcji (lista): {moja_lista}\n")  

#test liczby  
moja_liczba = 42
zmien_wartosc(moja_liczba)
print(f"Po wywolaniu funkcji (liczba): {moja_liczba}\n")