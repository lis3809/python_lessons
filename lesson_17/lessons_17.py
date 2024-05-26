import pygame

pygame.init()

high = 500
width = 500

rad = 50

window = pygame.display.set_mode((high, width))

# Координаты фигуры
x = 100
y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    elif keys[pygame.K_UP]:
        y -= 3
    elif keys[pygame.K_DOWN]:
        y += 3

    window.fill('white')

    pygame.draw.circle(window, (255, 255, 0), (x, y), rad)
    pygame.display.update()

    pygame.time.delay(10)
