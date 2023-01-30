import pygame
from tablero import *
import pieza

#Iniciamos y hacemos los ajustes de la ventana y la inicialización de variables que usaremos
pygame.init()

WIDTH, HEIGHT = 200, 400
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Tetris de Manu")

jugando = True
tablero = Tablero()

#Ponemos los corchetes esos al final para hacer una copia del array y así no poder modificar los colores
coloresDePiezas = Pieza.colores[:]

while jugando:
    #Creamos una pieza solo al iniciarlo ya que es el único momento en el que está nula
    if tablero.pieza == None:
        tablero.crearFigura()
    
    if tablero.modo == 1:
        tablero.bajarPieza()

    for e in pygame.event.get():
        if e.type == pygame.QUIT: #Cerramos la ventana por lo que salimos del bucle
            jugando = False

        if e.type == pygame.KEYDOWN: #Comprobamos si se ha pulsado alguna tecla
            if e.key == pygame.K_UP or e.key == pygame.K_w: #Llamamos al evento que hace que gire la pieza
                tablero.girarPieza()

            if e.key == pygame.K_LEFT or e.key == pygame.K_a: #Llamamos al evento que realiza el movimiento lateral de la pieza y le ponemos un valor negativo para que se mueva a la izquierda
                tablero.movLateral(-1)

            if e.key == pygame.K_RIGHT or e.key == pygame.K_d: #Llamamos al evento que realiza el movimiento lateral de la pieza y le ponemos un valor positivo para que se mueva a la derecha
                tablero.movLateral(1)

            if e.key == pygame.K_DOWN or e.key == pygame.K_s: #Llamamos al evento que baja la pieza con mayor número para que baje más deprisa
                tablero.bajarPieza()
                tablero.bajarPieza()
                tablero.bajarPieza()

            if e.key == pygame.K_r:
                tablero.__init__()
    
    ventana.fill((0, 0, 0))
        
    for i in range(tablero.alto):
        for j in range(tablero.ancho):
            #Recorremos nuestras variables de las dimensiones del tablero para hacer rectángulos con borde y vacíos
            pygame.draw.rect(ventana, (255, 255, 255), [tablero.tamanyoCelda * j, tablero.tamanyoCelda * i, tablero.tamanyoCelda, tablero.tamanyoCelda], 1)

            #Comprobamos si la celda que toca tiene un trozo de pieza y si es así hacemos un rectángulo de color
            if tablero.filas[i][j] > 0:
                pygame.draw.rect(ventana, coloresDePiezas[tablero.filas[i][j]], [tablero.tamanyoCelda * j + 1,tablero.tamanyoCelda * i + 1, tablero.tamanyoCelda - 2, tablero.tamanyoCelda - 2])

    if tablero.pieza != None:
        for i in range(4):
            for j in range(4):
                if i * 4 + j in tablero.pieza.limitePieza():
                    pygame.draw.rect(ventana, coloresDePiezas[tablero.pieza.colorPieza], [tablero.tamanyoCelda * (j + tablero.pieza.x) + 1, tablero.tamanyoCelda * (i + tablero.pieza.y) + 1, tablero.tamanyoCelda - 2, tablero.tamanyoCelda - 2])

    fuenteGameOver = pygame.font.Font(None, 53)
    txtGameOver = fuenteGameOver.render("Game Over", True, (255,105,180))

    if tablero.modo == 0:
        ventana.blit(txtGameOver, [0, 150])

    pygame.display.flip()
    pygame.time.Clock().tick(10)

pygame.quit()
