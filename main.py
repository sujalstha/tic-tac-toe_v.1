import pygame
import sys

pygame.init()

Width = 500
Height = 500

window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Tic-Tac-Toe v.1')

# mainloop for running the game

while True:
    for game in pygame.event.get():
        if game.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()