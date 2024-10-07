class Kareler:
    def __init__(self, _max):
        self.max = _max
        self.kare = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.kare <= self.max:
            sonuc = self.kare ** 2
            self.kare += 1
            return sonuc
        else:
            raise StopIteration


kare = Kareler(5)

for i in kare:
    print(i)
