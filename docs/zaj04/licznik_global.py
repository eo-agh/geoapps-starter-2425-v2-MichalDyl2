count_global = 0

def licznik_global():
    global count_global
    count_global += 1
    return count_global

# Test:
print(licznik_global())  # 1
print(licznik_global())  # 2
