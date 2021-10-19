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

print(calculateDistance(wierzcholki[0].wspolrzednaX, wierzcholki[0].wspolrzednaY, wierzcholki[1].wspolrzednaX, wierzcholki[1].wspolrzednaY))