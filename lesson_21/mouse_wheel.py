import pygame

pygame.init()

high = 500
width = 500

FPS = 30
clock = pygame.time.Clock()

rad = 50

window = pygame.display.set_mode((high, width))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEWHEEL:
            print(event.x, event.y)

    window.fill('white')

    pygame.display.update()
    clock.tick(FPS)
