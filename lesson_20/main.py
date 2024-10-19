import pygame
from mySuperCircle import MySuperCircle

pygame.init()

high = 500
width = 500

FPS = 30
clock = pygame.time.Clock()

centr_x = width // 2
centr_y = high // 2

rad = 50

window = pygame.display.set_mode((high, width))

myCircle = MySuperCircle(centr_x, centr_y, rad, 'red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill('white')

    myCircle.move_by_keys()
    myCircle.draw(window)

    pygame.display.update()

    pygame.time.delay(10)
    # clock.tick(FPS)
