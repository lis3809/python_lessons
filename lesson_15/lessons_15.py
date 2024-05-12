import pygame

pygame.init()
window = pygame.display.set_mode((600, 400))

color = (255, 255, 255)
window.fill(color)

pygame.draw.rect(window, (255, 255, 0), (50, 50, 200, 100))

pygame.draw.circle(window, 'green', (350, 350), 50)

pygame.draw.polygon(window, 'black', [(0, 100), (100, 50), (100, 150)], True)

pygame.draw.line(window, 'red', (0, 0), (200, 400), 5)

pygame.draw.lines(window, 'blue', True, ((150, 200), (150, 350), (400, 400)))

pygame.display.update()

x = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x += 0.01
    pygame.draw.circle(window, 'green', (x, x), 50)
    pygame.display.update()
