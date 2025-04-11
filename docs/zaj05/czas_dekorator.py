import time 

def zmierz_czas(unit='seconds'):
    def dekorator(funkcja):
        def wrapper(*args, **kwargs):
            start = time.time()  
            wynik = funkcja(*args, **kwargs) 
            end = time.time()  
            czas = end - start
return  
           