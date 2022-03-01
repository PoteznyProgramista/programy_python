import turtle
import random

w = 750
offset_y = -250
punkty = [
    (-w/2, offset_y), 
    (w/2, offset_y), 
    (0, w/2 * 3**.5 + offset_y)]

t = turtle.Turtle()
t.up()
t.speed(0)


def srednia_punktow(punkt1, punkt2, r=.5):
    return (
        punkt1[0] * (1 - r) + punkt2[0] * r,
        punkt1[1] * (1 - r) + punkt2[1] * r
    )

def odleglosc2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def najblizszy_punkt(punkt, punkty):
    def funkcja_pomocnicza_do_porownania(p):
        return odleglosc2(p, punkt)

    return min(punkty, key=funkcja_pomocnicza_do_porownania)



def moj_max(sekwencja, klucz):
    sekwencja_na_wartosci = [klucz(element) for element in sekwencja]
    max_i = 0
    for i in range(1, len(sekwencja)):
        if sekwencja_na_wartosci[max_i] < sekwencja_na_wartosci[i]:
            max_i = i
    return sekwencja[max_i]

lista = [(10, 10), (20, 2), (-5, 50)]
def suma_elementow(krotka):
    return krotka[0] + krotka[1]
#print(moj_max(lista, suma_elementow))


start = punkty[0]
t.setposition(start)
while True:
    p = random.choice(punkty)
    s = srednia_punktow(start, p)
    t.setposition(s)
    najbl = najblizszy_punkt(s, punkty)
    if najbl == punkty[0]:
        t.color("green")
    elif najbl == punkty[1]:
        t.color("blue")
    else:
        t.color("red")
    t.dot(size=3)
    start = s
