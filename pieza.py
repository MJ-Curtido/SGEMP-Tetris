from random import *

class Pieza:
    x = 0
    y = 0

    piezas = [
        [[4, 5, 6, 7], [1, 5, 9, 13]], #paloV, paloH
        [[0, 1, 4, 5]], #cuadrado
        [[0, 5, 9,  10], [4, 0, 1, 2], [0, 1, 5, 9], [4, 5, 6, 2]] #lNormal, lAbajoH, LPrima, lArribaH
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pieza = randint(0, len(self.piezas) - 1)
        self.posicion = 0

    def limitePieza(self):
        return self.piezas[self.pieza][self.posicion]

    def girarPieza(self):
        if self.posicion + 1 == len(self.piezas):
            self.posicion = 0;
        else:
            self.posicion = self.posicion + 1
