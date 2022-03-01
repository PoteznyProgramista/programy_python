
from matplotlib import pyplot as plt
import random


def policz_blad(X, Y, a, b):
    wynik = 0
    for i in range(len(X)):
        wynik += (a*X[i] + b - Y[i])**2
    return wynik/len(X)


def wyswietl_punkty_i_linie(X, Y, a, b):
    # X = [x_1, x_2, x_3, ..., x_n]
    # Y = [y_1, y_2, y_3, ..., y_n]
    # a,b to wspolczynniki prostej
    plt.scatter(X, Y, s=5, c='black', marker='o')
    min_x = min(X)
    max_x = max(X)
    plt.axline((min_x, a * min_x + b), (max_x, a *
               max_x + b), linewidth=2, color='r')
    blad = policz_blad(X, Y, a, b)
    plt.title(f'a={a:.4f} b={b:.4f} blad={blad:.4f}')


def generuj_x_punktow(n, x_start=0):
    return [x + x_start for x in range(n)]
    # X = []
    # for _ in range(n):
    #     X.append(random.randint(0, 100))
    # return X


def generuj_y_punktow(X, a=3, b=-2, rozrzut=20):
    Y = []
    for x in X:
        Y.append(a * x + b + (random.random() - 0.5) * rozrzut)
    return Y
#wyswietl_punkty_i_linie(X, Y, a, b)
# print(generuj_x_punktow(10))
# print(generuj_y_punktow(10))


def korygowanie_prostej(X, Y):
    a = random.random()
    b = random.random()
    alfa = 0.00001
    n = len(X)
    for _ in range(100):
        grad_a = 0
        grad_b = 0
        for i in range(n):
            y_hat = a * X[i] + b
            grad_a += X[i] * (y_hat - Y[i])
            grad_b += y_hat - Y[i]
        grad_a = (grad_a*2)/n
        grad_b = (grad_b*2)/n
        a -= grad_a * alfa
        b -= grad_b * alfa
        wyswietl_punkty_i_linie(X, Y, a, b)
        plt.pause(0.1)
        plt.clf()

    plt.show()


X = generuj_x_punktow(100, x_start=-50)
Y = generuj_y_punktow(X,
                      a=(random.random() - 0.5) * 20,
                      b=(random.random() - 0.5) * 20,
                      rozrzut=100
                      )
korygowanie_prostej(X, Y)
