import pygame
import time

window = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Python Game')
window.fill((235,50,200))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pass
        pass
    pygame.display.update()
