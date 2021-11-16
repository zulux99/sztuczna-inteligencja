import random
# def yFunkcji(a, b, c, d):
#     return a
print("Podaj wartości funkcji ax^3 + bx^2 + cx + d")
# a = input("Podaj a: ")
# b = input("Podaj b: ")
# c = input("Podaj c: ")
# d = input("Podaj d: ")
# Pk = input("Podaj Pk: ")
# Pm = input("Podaj Pm: ")
chromosomy = []
for i in range(0,6):
    chromosomy.append(format(random.randint(0, 31), "06b"))
for i in chromosomy:
    print(i)