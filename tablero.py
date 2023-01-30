from pieza import *
#py -m pip install pygame --pre
class Tablero:
    level = 2
    puntuacion = 0
    modo = 1
    filas = []
    alto = 0
    ancho = 0
    x = 100
    y = 60
    zoom = 20
    pieza = None

    def __init__(self):
        self.alto = 20
        self.ancho = 10
        self.filas = []
        self.puntuacion = 0
        self.modo = 1

        #Creamos el tablero según las dimensiones establecidas arriba, creando filas rellenas de ceros y guardándolas en el array de filas
        for i in range(self.alto):
            linea = []

            for j in range(self.ancho):
                linea.append(0)

            self.filas.append(linea)

    #Método que crea figuras cada vez que lo llame, estableciendo la x e y en la primera fila aproximadamente en el medio
    def crearFigura(self):
        self.pieza = Pieza(3, 0)

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
                #Comprobamos que la celda esté dentro de la figura
                if i * 4 + j in self.pieza.image():
                    self.filas[i + self.pieza.y][j + self.pieza.x] = self.pieza.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.modo = 0

    def movLateral(self, nuevaX):
        antiguaX = self.pieza.x
        self.pieza.x += nuevaPos
        if self.dentroDeLimite():
            self.pieza.x = antiguaX

    def rotate(self):
        old_rotation = self.pieza.rotation
        self.pieza.rotate()
        if self.intersects():
            self.pieza.rotation = old_rotation
