import random

import pygame as pg

pg.init()

# Высота и ширина окна
hight = 500
width = 500

FPS = 30
clock = pg.time.Clock()

# Различные переменные
GRAY = [70] * 3
BLACK = [0] * 3
WHITE = [255] * 3

# Основное окно
window = pg.display.set_mode((width, hight))
# Закрашиваем фон
window.fill(BLACK)

# Запускаем главный цикл
while True:

    """ Начало игровой логики  """
    # Обрабатываем события (мышки, клавиатуры...)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


    # Различные игровые события
    # Отрисовываем случайные звезды
    for i in range(10):
        pg.draw.circle(window, GRAY,
                       (random.randint(0, width), (random.randint(0, hight))),
                       1)

    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(window, WHITE, pos, 5)


    """ Конец игровой логики  """
    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)
