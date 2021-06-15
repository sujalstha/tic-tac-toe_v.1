import pygame
import sys
import numpy as np

pygame.init()

Width = 450
Height = 450
Line_Width = 10

# colors
BG_COLOR = (193, 125, 189)
LINE_COLOR = (202, 158, 200)

window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('TIC TAC TOE v.1')
window.fill(BG_COLOR)

board = np.zeros((3, 3))
print(board)


def lines():
    pygame.draw.line(window, LINE_COLOR, (0, 150), (500, 150), Line_Width)
    pygame.draw.line(window, LINE_COLOR, (0, 300), (500, 300), Line_Width)
    pygame.draw.line(window, LINE_COLOR, (150, 0), (150, 500), Line_Width)
    pygame.draw.line(window, LINE_COLOR, (300, 0), (300, 500), Line_Width)


lines()

# mainloop for running the game
while True:
    for game in pygame.event.get():
        if game.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
