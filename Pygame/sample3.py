import sys
import pygame
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animação')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.jpg')
catImg = pygame.transform.scale(catImg, (160, 130))
catx = 10
caty = 10
direction = 'right'

# Game.
while True:
    DISPLAYSURF.fill(WHITE)  # Fundo branco.

    if direction == 'right':
        catx += 5
        if catx == 260:
            direction = 'down'

    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'

    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'

    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)