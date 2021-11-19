import random

class Osobnik:
    def __init__(self, fenotyp, wartosc, procentNaKole = None):
        self.fenotyp = fenotyp
        self.wartosc = wartosc
        self.procentNaKole = procentNaKole
    def __repr__(self) -> str:
        return "CH = " + str(self.fenotyp) + " | Fenotyp " + str(int(self.fenotyp, 2)) + " | F.przyst = " + str(self.wartosc) + " | Koło: " + str(self.procentNaKole) + "\n"

# Obliczanie wartości Y z podanej funkcji f(x)
def wynikFunkcji(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d

# Funkcja losuje i zwraca 1 osobnika z koła ruletki
def losuj(populacja):
    losowa = random.randint(0, 100)
    if losowa >= 100:
        return populacja[5]
    suma = 0
    for i in populacja:
        suma = suma + i.procentNaKole
        if suma > losowa:
            return i

# Losuje nowych potomków, korzystając z koła ruletki
def funkcjaPrzystosowania(populacja):
    wylosowane = []
    for i in populacja:
        wylosowane.append(losuj(populacja))
    populacja = wylosowane
    przelicz(populacja)
    return populacja

# Krzyżowanie
def krzyzowanie(populacja, Pk):
    for i in range(0, int(len(populacja)), 2):
        PkWylosowane = random.randint(0, 10) / 10
        L = random.randint(0, 4)
        x = list(populacja[i].fenotyp)
        y = list(populacja[i + 1].fenotyp)
        if (PkWylosowane < Pk):
            x[L:], y[L:] = y[L:], x[L:]
        x = ''.join(x)
        y = ''.join(y)
        populacja[i].fenotyp = x
        populacja[i + 1].fenotyp = y
        przelicz(populacja)
    return populacja

# Mutacja
def mutacja(populacja, Pm):
    for i in populacja:
        PmWylosowane = random.randint(0, 10) / 10
        L = random.randint(0, 4)
        x = list(i.fenotyp)
        if (PmWylosowane < Pm):
            if x[L] == "1":
                x[L] = "0"
            else:
                x[L] = "1"
            x = ''.join(x)
            i.fenotyp = x
    przelicz(populacja)
    return populacja

# Funkcja przelicza wartości Y oraz procenty na kole ruletki dla całej populacji
def przelicz(populacja):
    global a, b, c, d
    for i in populacja:
        i.wartosc = wynikFunkcji(a, b, c, d, int(i.fenotyp, 2))
    suma = 0
    for i in populacja:
        suma = suma + i.wartosc
    for i in populacja:
        i.procentNaKole = i.wartosc / suma * 100
    return populacja

# Początek programu, wpisywanie zmiennych
print("Podaj wartości funkcji ax^3 + bx^2 + cx + d")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
d = float(input("Podaj d: "))
Pk = float(input("Podaj Pk (zakres 0-1): "))
Pm = float(input("Podaj Pm (zakres 0-1): "))
zatrzymanie = int(input("Podaj liczbę wystąpień największej sumy funkcji przystosowania: "))
pokazKazdaIteracje = input("Czy wyświetlić każdą iterację? Podaj t lub n: ")

# Stworzenie losowej populacji
populacja = []
for i in range(0, 6):
    random5bitBinaryNumber = format(random.randint(0, 31), "05b")
    wartoscY = round(wynikFunkcji(a, b, c, d, int(random5bitBinaryNumber, 2)), 2)
    populacja.append(Osobnik(random5bitBinaryNumber, wartoscY))

# Główny program
maksymalnaSuma = 0
licznik = 0
licznikIteracji = 0
while licznik < zatrzymanie:
    maksAktualny = 1
    licznikIteracji += 1
    populacja = przelicz(populacja)
    populacja = funkcjaPrzystosowania(populacja)
    populacja = krzyzowanie(populacja, Pk)
    populacja = mutacja(populacja, Pm)
    if pokazKazdaIteracje == "t":
        print(populacja, "\n")
    for i in populacja:
        maksAktualny += i.wartosc
    if maksymalnaSuma == maksAktualny:
        licznik += 1
    if maksymalnaSuma < maksAktualny:
        maksymalnaSuma = maksAktualny
if pokazKazdaIteracje == "n":
    print(populacja)
print("MAKS:", maksymalnaSuma)
print("Licznik:", licznikIteracji)