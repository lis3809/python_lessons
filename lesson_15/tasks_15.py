"""
Задание 1:
Напишите программу, которая считывает через стандартный поток ввода два целых числа,
разделенных пробелом, и создает средствами библиотеки PyGame черное окно заданного
размера, «перечеркнутое» белыми диагоналями толщиной в 5 пикселей.
"""

# import pygame
#
# string = input('Enter two numbers')
# list = string.split()
# width = int(list[0])
# height = int(list[1])
#
# pygame.init()
# window = pygame.display.set_mode((width, height))
#
# pygame.draw.line(window, (255, 255, 255), (0, 0), (width, height), 5)
# pygame.draw.line(window, (255, 255, 255), (0, height), (width, 0), 5)
#
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()


"""
Задание 2:
Напишите программу, которая считывает через стандартный поток ввода два целых числа, 
разделенных пробелом: 
размер стороны окна в пикселях а и количество клеток n (а кратно n) 
и создает средствами библиотеки PyGame квадратное окно а * а пикселей. 
Окно закрашивается в шахматную черно-белую клетку (n * n клеток), 
левая нижняя клетка должна быть черной.

В случае, если пользователь ввел неверные значения (не целые числа или в неправильном формате) 
программа должна печатать в командную строку сообщение «Неправильный формат ввода» 
и завершать работу.

Например, при вводе «250 5»
"""

# import pygame
#
# string = input('Enter two numbers')
# list = string.split()
# a = int(list[0])
# n = int(list[1])
#
# cell_size = a // n
#
#
# pygame.init()
# window = pygame.display.set_mode((a, a))
#
# for i in range(n):
#     for j in range(n):
#         if (i + j) % 2 == 0: # черно-белые клетки
#             pygame.draw.rect(window, 'black', (i * cell_size, j * cell_size, cell_size, cell_size))
#         else:
#             pygame.draw.rect(window, 'white', (i * cell_size, j * cell_size, cell_size, cell_size))
#
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()


"""
Задание 3:
Напишите программу, которая считывает через стандартный поток ввода целое число и рисует 
средствами библиотеки PyGame в окне 300 х 300 пикселей «проволочную» сферу из п горизонтальных 
и вертикальных белых эллипсов толщиной в 1 пиксель.

В случае, если пользователь ввел неверное значение (не целое число), программа должна 
печатать в командную строку сообщение «Неправильный формат ввода» и завершать работу.
"""

# import pygame
#
# string = input('Enter number')
# n = int(string)
#
# width = 300
# height = 300
#
# step_x = width // n
# step_y = height // n
#
# pygame.init()
# window = pygame.display.set_mode((width, height))
#
# for i in range(n):
#     pygame.draw.ellipse(window, 'white', (0 + (step_x * i) / 2, 0, width - step_x * i, height), 1)
#     pygame.draw.ellipse(window, 'white', (0, 0 + (step_y * i) / 2, width, height - step_y * i), 1)
#
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
