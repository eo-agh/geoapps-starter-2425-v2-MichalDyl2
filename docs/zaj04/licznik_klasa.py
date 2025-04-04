class Licznik:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

# Test:
l3 = Licznik()
print(l3())  # 1
print(l3())  # 2
