from random import *

class Pieza:
    #Hago un array con las piezas que quiero y con su número representado en una matriz:
    #   0  1  2  3
    #   4  5  6  7
    #   8  9  10 11
    #   12 13 14 15
    piezas = [
        [[0, 0, 0, 0]], #Ésta fila no cuenta como figura, simplemente es para que al rellenar la celda con un número, el que esté asignado con la figura aleatoria, para que no sea 0 ese número
        [[4, 5, 6, 7], [1, 5, 9, 13]], #paloV, paloH
        [[1, 2, 5, 6]], #cuadrado
        [[1, 5, 9,  10], [4, 0, 1, 2], [1, 2, 6, 10], [4, 5, 6, 2]] #lNormal, lAbajoH, LPrima, lArribaH
    ]

    #Hago un array con los colores que quiero que tengan las piezas correspondientes
    colores = [
        (0, 0, 0), #Ésta fila no cuenta como color, está explicado en el de arriba, que ocurre igual que en las piezas
        (255, 0, 0), #palo
        (0, 255, 0), #cuadrado
        (0, 0, 255) #L
    ]

    def __init__(self):
        #Genero un número aleatorio que posteriormente uso para coger la pieza con su color
        piezaColorRandom = randint(1, len(self.piezas) - 1)

        self.x = 3
        self.y = 0
        self.pieza = piezaColorRandom
        self.colorPieza = piezaColorRandom
        self.posicion = 0

    #Método con el cual devuelvo los límites de la pieza, que son los números que la componen (los que están en el array sacados de la matriz)
    def limitePieza(self):
        return self.piezas[self.pieza][self.posicion]

    #Método para girar la pieza, cambia la posición en la que se encuentra teniendo en cuenta de que si es la posición final, vuelva a la primera
    def cambiarPos(self):
        if self.posicion + 1 == len(self.piezas[self.pieza]):
            self.posicion = 0
        else:
            self.posicion = self.posicion + 1
