import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

while True:

    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #draw and update
    pygame.display.update()
    clock.tick(60)