import pygame

meu_nome = 'Felipe Lopes'
pygame.init()
minha_fonte = pygame.font.SysFont('arial', 64)
superficie_nome = minha_fonte.render(meu_nome, True, (0, 0, 0), (255, 255, 255))
pygame.image.save(superficie_nome, 'nome.png')