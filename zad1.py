class Wierzcholek:
    def __init__(self, wspolrzednaX, wspolrzednaY, id):
        self.id = id
        self.odwiedzony = False
        self.wspolrzednaX = wspolrzednaX
        self.wspolrzednaY = wspolrzednaY
    def __repr__(self):
        return str(self.id) + " = [" + str(self.wspolrzednaX) + "," + str(self.wspolrzednaY) + "]"

def inputInteger(message):
    while(True):
        try:
            x = int(input(message))
        except ValueError:
            print("Podana wartość nie jest liczbą całkowitą")
            continue
        else:
            return x

def calculateDistance(ax, ay, bx, by):
    distance = pow(pow(bx - ax, 2) + pow(by - ay, 2), 1/2)
    return distance

def shortestPath(punktStartowy, lista):
    najkrotszaOdlegosc = 5125152124789
    aktualnaOdleglosc = najkrotszaOdlegosc + 1
    for i in lista:
        if punktStartowy.id != i.id and i.odwiedzony == False:
            aktualnaOdleglosc = calculateDistance(punktStartowy.wspolrzednaX, punktStartowy.wspolrzednaY, i.wspolrzednaX, i.wspolrzednaY)
            punktStartowy.odwiedzony = True
            if najkrotszaOdlegosc > aktualnaOdleglosc:
                najkrotszaOdlegosc = aktualnaOdleglosc
                najblizszyWierzcholek = i
    return najblizszyWierzcholek, najkrotszaOdlegosc

def inputLetter(message):
    while(True):
        try:
            x = str(input(message))
        except ValueError:
            print("Podana wartość nie jest literą")
        else:
            return x

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
wierzcholki = []
while(True):
    iloscWierzcholkow = inputInteger("Podaj liczbę wierzchołków: ")
    if (iloscWierzcholkow < 2):
        print("Musisz podać minimum dwa wierzchołki")
        continue
    else:
        break
for i in range(iloscWierzcholkow):
    tempX = inputInteger("Podaj współrzędną X: ")
    tempY = inputInteger("Podaj współrzędną Y: ")
    wierzcholki.append(Wierzcholek(tempX, tempY, alfabet[i : i + 1]))
del tempX, tempY
print ("Podałeś następujące wierzchołki: ")
for obiekt in wierzcholki:
	print(obiekt)
literaWierzcholkaStartowego = inputLetter("Podaj literę wierzchołka startowego: ").upper()
print(literaWierzcholkaStartowego, "->", end=' ')
for i in wierzcholki:
    if i.id == literaWierzcholkaStartowego:
        wierzcholekStartowy = i
suma = 0
for i in wierzcholki:
    if i == wierzcholki[0]:
        nastepnyWierzcholek, odleglosc = shortestPath(wierzcholekStartowy, wierzcholki)
        print(nastepnyWierzcholek.id, "->", end=' ')
    elif i == wierzcholki[-1]:
        odleglosc = calculateDistance(nastepnyWierzcholek.wspolrzednaX, nastepnyWierzcholek.wspolrzednaY, wierzcholekStartowy.wspolrzednaX, wierzcholekStartowy.wspolrzednaY)
    else:
        nastepnyWierzcholek, odleglosc = shortestPath(nastepnyWierzcholek, wierzcholki)
        print(nastepnyWierzcholek.id, "->", end=' ')
    suma += odleglosc
print(wierzcholekStartowy.id)
print(f"Odległość: {suma}")