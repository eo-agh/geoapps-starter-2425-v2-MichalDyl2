def licznik_nonlocal():
    count = 0
    def zwieksz():
        nonlocal count
        count += 1
        return count
    return zwieksz

# Test:
l1 = licznik_nonlocal()
print(l1())  # 1
print(l1())  # 2
