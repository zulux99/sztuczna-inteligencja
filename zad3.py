import random
import copy
class Osobnik:
    def __init__(self, chromosom, waga = 0, wartosc = 0, procentNaKole = 0):
        self.chromosom = chromosom
        self.procentNaKole = procentNaKole
        self.waga = waga
        self.wartosc = wartosc
    def __repr__(self) -> str:
        return "CH = " + str(self.chromosom) + " | waga " + str(self.waga) + " | wartosc = " + str(self.wartosc) + " | Koło: " + str(self.procentNaKole) + "\n"

global populacja, Pk, Pm, wagaMax
populacja = []

def przelicz():
    wartoscWszystkichChromosomow = 0
    for i in populacja:
        wagaChromosomu = 0
        wartoscChromosomu = 0
        iloscJedynek = 0
        for j in range(0, 10):
            if i.chromosom[j : j + 1] == "1":
                iloscJedynek += 1
                wagaChromosomu += wagaWszystkich[j]
                wartoscChromosomu += wartoscWszystkich[j]
        if wagaChromosomu > wagaMax:
            losowyBit = random.randint(1, iloscJedynek)
            licznik = 1
            for j in range(0, 10):
                if i.chromosom[j : j + 1] == "1":
                    if licznik == losowyBit:
                        temp = list(i.chromosom)
                        temp[j] = "0"
                        i.chromosom = ''.join(temp)
                        return przelicz()
                    licznik += 1
        i.waga = wagaChromosomu
        i.wartosc = wartoscChromosomu
        wartoscWszystkichChromosomow += i.wartosc
    suma = 0
    if wartoscWszystkichChromosomow != 0:
        for i in populacja:
            i.procentNaKole = i.wartosc / wartoscWszystkichChromosomow * 100
            suma += i.procentNaKole

def przystosuj():
    wylosowane = []
    for i in range(0, len(populacja)):
        suma = 0
        losowa = random.randint(0, 100)
        if losowa >= 100:
            wylosowane.append(populacja[-1])
            break
        for j in populacja:
            suma += j.procentNaKole
            if suma > losowa:
                wylosowane.append(copy.deepcopy(j))
                break
    for a in range(0, len(wylosowane)):
        populacja[a] = wylosowane[a]
    del wylosowane

def krzyzowanie():
    for i in range(0, int(len(populacja)), 2):
        PkWylosowane = random.randint(0, 100) / 100
        if (PkWylosowane < Pk):
            L = random.randint(1, 9)
            x = list(populacja[i].chromosom)
            y = list(populacja[i + 1].chromosom)
            x[L:], y[L:] = y[L:], x[L:]
            x = ''.join(x)
            y = ''.join(y)
            populacja[i].chromosom = x
            populacja[i + 1].chromosom = y

def mutacja():
    for i in populacja:
        PmWylosowane = random.randint(0, 100) / 100
        if (PmWylosowane < Pm):
            L = random.randint(0, 9)
            x = list(i.chromosom)
            if x[L] == "1":
                x[L] = "0"
            else:
                x[L] = "1"
            x = ''.join(x)
            i.chromosom = x
    
wagaWszystkich = [12, 4, 12, 5, 8, 15, 18, 10, 8, 9]
wartoscWszystkich = [6, 15, 10, 14, 6, 12, 5, 8, 13, 6]
wagaMax = 59
Pk = 0.8
Pm = 0.2
for i in range(0, 6):
    losowa10BitowaLiczbaBinarna = format(random.randint(0, 1023), "010b")
    waga = wagaWszystkich[i]
    wartosc = wartoscWszystkich[i]
    populacja.append(Osobnik(losowa10BitowaLiczbaBinarna))
del waga, wartosc, losowa10BitowaLiczbaBinarna
licznikIteracji = 0
najwiekszaWartosc = 0
zatrzymanie = int(input("Podaj ilość wystąpień najwyższej wartości: "))
licznikWystapienNajwyzszejWartosci = 0
while licznikWystapienNajwyzszejWartosci < zatrzymanie:
    licznikIteracji += 1
    przelicz()
    przystosuj()
    krzyzowanie()
    przelicz()
    mutacja()
    przelicz()
    for i in populacja:
        if najwiekszaWartosc < i.wartosc:
            najwiekszaWartosc = i.wartosc
            licznikWystapienNajwyzszejWartosci = 1
            najlepszyOsobnik = i
        if najwiekszaWartosc == i.wartosc:
            licznikWystapienNajwyzszejWartosci += 1
print("Ilość iteracji:", licznikIteracji)
print(najlepszyOsobnik)