import pygame
from pygame.locals import *
import sys

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

# Criar um objeto do tipo 'Font'.
fontObj = pygame.font.Font('freesansbold.ttf', 32)
# Criar um objeto 'Surface' com texto escrito usando o método 'render()'.
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)  # O True serve para ligar o anti-aliasing, para deixar mais limpo cada conjunto de pixels.
# Criar o objeto 'Rect' usando 'get_rect()' do objeto 'Surface'.
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:  # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
