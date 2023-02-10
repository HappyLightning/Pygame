import pygame
import sys

pygame.init()  # Inicializa cada módulo.

size = width, height = 1080, 800
speed = [2, 2]
black = 0, 0, 0

# Cria uma janela gráfica.
screen = pygame.display.set_mode(size)

# Adicionamos nossa bola.
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()  # Representa uma área retangular na nossa bola.

# Programa inicializado e pronto para rodar.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
