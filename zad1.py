class Wierzcholek:
    def __init__(self, wspolrzednaX, wspolrzednaY, id):
        self.id = id
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
    najkrotszaOdlegosc = 0
    najblizszyWierzcholek = punktStartowy.id
    for i in lista:
        aktualnaOdleglosc = calculateDistance(punktStartowy.wspolrzednaX, punktStartowy.wspolrzednaY, i.wspolrzednaX, i.wspolrzednaY)
        if i == 0 and aktualnaOdleglosc != 0:
            najkrotszaOdlegosc = aktualnaOdleglosc
        elif najkrotszaOdlegosc > aktualnaOdleglosc:
            najkrotszaOdlegosc = aktualnaOdleglosc
            najblizszyWierzcholek = i.id
    return najblizszyWierzcholek

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
wierzcholekStartowy = inputLetter("Podaj literę wierzchołka startowego: ")
print(shortestPath(wierzcholki[0], wierzcholki))
