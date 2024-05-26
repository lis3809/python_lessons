"""
Задание 1:
Напишите программу, в которой окружность появляется в центре окна,
размером 500 на 500 пикселей. У пользователя есть возможность
управлять окружностью с помощью стрелок, но как только пользователь
отпускает стрелки (после вывода окружности из центра окна), окружность
возвращается в центр окна “сама” (пользователь в этом процессе не участвует).
"""
#
# import pygame
#
# pygame.init()
#
# high = 500
# width = 500
#
# centr_x = width//2
# centr_y = high//2
#
# rad = 50
#
# window = pygame.display.set_mode((high, width))
#
# # Координаты фигуры
# x = centr_x
# y = centr_y
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         x -= 3
#     elif keys[pygame.K_RIGHT]:
#         x += 3
#     elif keys[pygame.K_UP]:
#         y -= 3
#     elif keys[pygame.K_DOWN]:
#         y += 3
#     else:
#         x = centr_x
#         y = centr_y
#
#     # if not any(keys):
#     #     x = centr_x
#     #     y = centr_y
#
#     window.fill('white')
#
#     pygame.draw.circle(window, (255, 255, 0), (x, y), rad)
#     pygame.display.update()
#
#     pygame.time.delay(10)
#

"""
Задание 2:
Допишите предыдущую программу, чтобы при удалении от центра окна 
на 150 пикселей цвет окружности меняется на красный и скорость, 
с которой перемещается окружность становится меньше.
"""

# import pygame
#
# pygame.init()
#
# high = 500
# width = 500
#
# centr_x = width // 2
# centr_y = high // 2
#
# rad = 50
#
# window = pygame.display.set_mode((high, width))
#
# # Координаты фигуры
# x = centr_x
# y = centr_y
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         x -= 3
#     elif keys[pygame.K_RIGHT]:
#         x += 3
#     elif keys[pygame.K_UP]:
#         y -= 3
#     elif keys[pygame.K_DOWN]:
#         y += 3
#     else:
#         x = centr_x
#         y = centr_y
#
#     window.fill('white')
#
#     if x > centr_x + 150 or x < centr_x - 150 or y > centr_y + 150 or y < centr_y - 150:
#         pygame.draw.circle(window, 'red', (x, y), rad)
#     else:
#         pygame.draw.circle(window, (255, 255, 0), (x, y), rad)
#
#     pygame.display.update()
#
#     pygame.time.delay(10)
