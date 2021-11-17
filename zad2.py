import random
class Osobnik:
    def __init__(self, fenotyp, wartosc, procentNaKole = None):
        self.fenotyp = fenotyp
        self.wartosc = wartosc
        self.procentNaKole = procentNaKole
    def __repr__(self) -> str:
        return "Fenotyp: " + str(self.fenotyp) + " o wartości: " + str(self.wartosc)
def wynikFunkcji(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d
def losuj(listaOsobnikow):
    losowa = random.randint(0, 100)
    if losowa >= 100:
        return listaOsobnikow[5]
    print(losowa)
    suma = 0
    for i in listaOsobnikow:
        suma = suma + i.procentNaKole
        if suma > losowa:
            return i
# def krzyzowanie():
# def mutacja():
print("Podaj wartości funkcji ax^3 + bx^2 + cx + d")
# a = float(input("Podaj a: "))
# b = float(input("Podaj b: "))
# c = float(input("Podaj c: "))
# d = float(input("Podaj d: "))
a = 0
b = 0
c = 0.2
d = 5
# Pk = input("Podaj Pk: ")
# Pm = input("Podaj Pm: ")
listaOsobnikow = []
for i in range(0, 6):
    random5bitBinaryNumber = format(random.randint(0, 31), "05b")
    wartoscY = round(wynikFunkcji(a, b, c, d, int(random5bitBinaryNumber, 2)), 2)
    listaOsobnikow.append(Osobnik(random5bitBinaryNumber, wartoscY))
suma = 0
for i in listaOsobnikow:
    suma = suma + i.wartosc
test = 0
for i in listaOsobnikow:
    i.procentNaKole = i.wartosc / suma * 100
    test = test + i.procentNaKole
print(losuj(listaOsobnikow))