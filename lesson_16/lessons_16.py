import pygame

pygame.init()

high = 500
width = 500

window = pygame.display.set_mode((high, width))

# Координаты фигуры
x = 100
y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = x + 1

    window.fill('white')

    pygame.draw.rect(window, (255, 255, 0), (x, y, 100, 150))
    pygame.display.update()

    pygame.time.delay(10)
