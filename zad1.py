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
            print("Podaj liczbę całkowitą: ")
            continue
        else:
            return x

def calculateDistance(ax, ay, bx, by):
    distance = pow(pow(bx - ax, 2) + pow(by - ay, 2), 1/2)
    return distance

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
wierzcholki = []
iloscWierzcholkow = inputInteger("Podaj liczbę wierzchołków: ")
for i in range(iloscWierzcholkow):
    tempX = inputInteger("Podaj współrzędną X: ")
    tempY = inputInteger("Podaj współrzędną Y: ")
    wierzcholki.append(Wierzcholek(tempX, tempY, alfabet[i : i + 1]))
del tempX, tempY
print ("Podałeś następujące wierzchołki: ")
for obiekt in wierzcholki:
    print(obiekt)
# TODO
calculateDistance(wierzcholki)