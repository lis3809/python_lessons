"""
Задание 1:
Напишите программу, в которой 2 объекта: окружность и прямоугольник.
Окружность двигается по вертикали (сверху вниз, при пересечении нижней грани окружность появляется сверху).
Прямоугольник двигается по горизонтали (слева направо, при пересечении правой грани прямоугольник появляется сверху).
"""
# import pygame
#
# pygame.init()
#
# high = 500
# width = 500
#
# window = pygame.display.set_mode((high, width))
#
# # Координаты фигур
# x_rec = 100
# y_rec = 100
#
# x_circle = 50
# y_circle = 50
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     x_rec = x_rec + 1
#
#     y_circle = y_circle + 1
#
#     if x_rec > width:
#         x_rec = 0
#
#     if y_circle > high:
#         y_circle = 0
#
#     window.fill('white')
#
#     pygame.draw.rect(window, (255, 255, 0), (x_rec, y_rec, 100, 150))
#     pygame.draw.circle(window, 'blue', (x_circle, y_circle), 50)
#     pygame.display.update()
#
#     pygame.time.delay(10)

"""
Задание 2:
Напишите программу, в которой 2 объекта: окружность и прямоугольник.
Окружность двигается по вертикали (сверху вниз, при касании нижней грани окружность начинается двигаться вверх).
Прямоугольник двигается по горизонтали (слева направо, при касании правой грани прямоугольник начинается двигаться влево).
"""

import pygame

pygame.init()

high = 500
width = 500

circle_radius = 50
rec_size = 100

window = pygame.display.set_mode((high, width))

# Координаты фигур
x_rec = 100
y_rec = 100

x_circle = 50
y_circle = 50

dir_rec = 1

dir_circle = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x_rec = x_rec + dir_rec

    y_circle = y_circle + dir_circle

    if x_rec >= width:
        dir_rec = -1
    if x_rec == 0:
        dir_rec = 1

    if y_circle >= high:
        dir_circle = -1
    if y_circle == 0:
        dir_circle = 1

    window.fill('white')

    pygame.draw.rect(window, (255, 255, 0), (x_rec, y_rec, rec_size, rec_size))
    pygame.draw.circle(window, 'blue', (x_circle, y_circle), circle_radius)
    pygame.display.update()

    pygame.time.delay(10)


"""
Задание 3:
Допишите предыдущую программу, в которой 2 объекта: окружность и прямоугольник, 
добавив в неё ещё 2 окружности, которые будут двигаться синхронно по диагоналям (сверху вниз).
"""
