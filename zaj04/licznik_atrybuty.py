def licznik_funkcyjny():
    licznik_funkcyjny.count += 1
    return licznik_funkcyjny.count

licznik_funkcyjny.count = 0

# Test:
print(licznik_funkcyjny())  # 1
print(licznik_funkcyjny())  # 2
