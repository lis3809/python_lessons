import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Click Counter')

clicks = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == MOUSEBUTTONDOWN:
            clicks += 1

    screen.fill((255, 255, 255))

    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Clicks: {clicks}', True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)