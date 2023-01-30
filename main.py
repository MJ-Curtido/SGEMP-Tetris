import pygame

WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Tetris Manu")

figures = [
    [[4, 5, 6, 7], [1, 5, 9, 13]], #vStick, hStick
    [[0, 1, 4, 5]], #square
    [[0, 5, 9,  10], [4, 0, 1, 2], [0, 1, 5, 9], [4, 5, 6, 2]] #normalL, hDownL, primeL, hUpL
]

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            ventana.fill((252, 243, 207))
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            pygame.quit()
