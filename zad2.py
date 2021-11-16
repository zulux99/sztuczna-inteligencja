import random
class Osobnik:
    def __init__(self, fenotyp, wartosc, procentNaKole = None):
        self.fenotyp = fenotyp
        self.wartosc = wartosc
        self.procentNaKole = procentNaKole
def wynikFunkcji(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d
# def krzyzowanie():
# def mutacja():
print("Podaj wartości funkcji ax^3 + bx^2 + cx + d")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
d = float(input("Podaj d: "))
# Pk = input("Podaj Pk: ")
# Pm = input("Podaj Pm: ")
listaOsobnikow = []
for i in range(0, 6):
    random5bitBinaryNumber = format(random.randint(0, 31), "05b")
    listaOsobnikow.append(Osobnik(random5bitBinaryNumber, round(wynikFunkcji(a, b, c, d, int(random5bitBinaryNumber, 2)), 2)))
suma = 0
for i in listaOsobnikow:
    suma = suma + i.wartosc
test = 0
for i in listaOsobnikow:
    i.procentNaKole = round(i.wartosc / suma * 100, 2)
    print(i.procentNaKole)
    test = test + i.procentNaKole
print(test)