class Calculator:
    def __init__(self):
        self.rezultat = 0

    def aduna(self, x, y):
        self.rezultat = x + y

    def scade(self, x, y):
        self.rezultat = x - y

    def inmulteste(self, x, y):
        self.rezultat = x * y

    def imparte(self, x, y):
        if y != 0:
            self.rezultat = x / y
        else:
            print("Impartirea la zero nu este permisa!")

    def afiseaza_rezultatul(self):
        print("Rezultatul este:", self.rezultat)
