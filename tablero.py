from pieza import *

class Tablero:
    level = 2
    tamanyoCelda = 20
    pieza = None

    def __init__(self):
        self.alto = 20
        self.ancho = 10
        self.filas = []
        self.modo = 1 #Modo = 1 => Continúa el juego; Modo = 2 => Juego terminado

        #Creamos el tablero según las dimensiones establecidas arriba, creando filas rellenas de ceros y guardándolas en el array de filas
        for i in range(self.alto):
            linea = []

            for j in range(self.ancho):
                linea.append(0)

            self.filas.append(linea)

    #Método que crea figuras cada vez que lo llame, estableciendo la x e y en la primera fila aproximadamente en el medio
    def crearFigura(self):
        self.pieza = Pieza()

    #Método que te devuelve si la pieza está fuera de los límites o no
    def fueraDeLimite(self):
        fuera = False
        #Recorremos nuestro esquema que contiene las figuras
        for i in range(4):
            for j in range(4):
                #Comprobamos todas las opciones por las cuales puede estar fuera de límite, ya sea fuera del tablero (por la derecha, izquierda o abajo), o con la colisión con otra figura, comprobando si en cada celda hay un 0 o un número mayor, lo que significaría que hay una figura
                if (i * 4 + j in self.pieza.limitePieza()) and (i + self.pieza.y > self.alto - 1 or j + self.pieza.x > self.ancho - 1 or j + self.pieza.x < 0 or self.filas[i + self.pieza.y][j + self.pieza.x] > 0):
                    fuera = True
        return fuera

    #Método que hace que baje la figura a no ser que se encuentre con una figura o se salga de los límites que entonces la para
    def bajarPieza(self):
        self.pieza.y = self.pieza.y + 1

        if self.fueraDeLimite():
            self.pieza.y = self.pieza.y - 1

            self.pararPieza()

    def pararPieza(self):
        #Recorremos nuestro esquema que contiene las figuras
        for i in range(4):
            for j in range(4):
                #Comprobamos que la celda esté dentro de la figura y la coloreamos
                if i * 4 + j in self.pieza.limitePieza():
                    self.filas[i + self.pieza.y][j + self.pieza.x] = self.pieza.colorPieza
        #Una vez parada, creamos una nueva figura que aparecerá arriba
        self.crearFigura()

        #Si esa figura nueva creada está fuera de los límites porque ya haya una figura ahí, hemos perdido y ponemos el modo en 0
        if self.fueraDeLimite():
            self.modo = 0

    #Método con el que movemos la pieza lateralmente en el caso de que no se salga de los límites ya sea fuera del tablero o chocándose con otra pieza
    def movLateral(self, nuevaX):
        antiguaX = self.pieza.x
        self.pieza.x += nuevaX

        if self.fueraDeLimite():
            self.pieza.x = antiguaX

    #Método con el que giramos la pieza en el caso de que no se salga de los límites ya sea fuera del tablero o chocándose con otra pieza
    def girarPieza(self):
        antiguaPos = self.pieza.posicion
        self.pieza.cambiarPos()

        if self.fueraDeLimite():
            self.pieza.posicion = antiguaPos
