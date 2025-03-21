def stworz_raport(*args, **kwargs):
    print("\nRAPORT PRODUKTOW:\n" + "="*30)

    for product_id in args:  #ITERACJA po ID
        nazwa_key = f"nazwa_{product_id}"
        cena_key = f"cena_{product_id}"  
        
        nazwa = kwargs.get( nazwa_key, "Nieznana nazwa" )  #pobieramy nazwe i cene, obie domyslnie nieznane
        cena = kwargs.get( cena_key, "Nieznana cena" ) 

        print(f"Produkt ID: {product_id}")
        print(f"Nazwa: {nazwa}")
        print(f"Cena: {cena}\n")

#Test f
stworz_raport(
    101, 102, 103,
    nazwa_101="Kubek termiczny", cena_101="45.99 zł",
    nazwa_102="Długopis", cena_102="4.99 zł",
    nazwa_103="Notes", cena_103="12.50 zł"
)
