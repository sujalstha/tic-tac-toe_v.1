import pygame
import sys

pygame.init()

Width = 500
Height = 500

# colors
BG_COLOR = (158, 124, 206)
BLUE = (124, 169, 206)
LINE_COLOR = (127, 197, 113)

window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Tic-Tac-Toe v.1')
window.fill(BG_COLOR)

pygame.draw.line(window, BLUE, (10, 10), (250, 250), 10)


def lines():
    pass


# mainloop for running the game
while True:
    for game in pygame.event.get():
        if game.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()