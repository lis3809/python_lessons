import pygame as pg

pg.init()

# Высота и ширина окна
height = 600
width = 600

FPS = 30
clock = pg.time.Clock()

# Различные переменные
BLACK = [0] * 3
GRAY = [100] * 3
WHITE = [255] * 3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTGREEN = (0, 200, 200)

# Основное окно
window = pg.display.set_mode((width, height))

# Запускаем главный цикл
while True:

    """ Начало игровой логики  """
    # Обрабатываем события (мышки, клавиатуры...)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Закрашиваем фон
    window.fill(WHITE)

    # Различные игровые события

    """ Конец игровой логики  """
    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)
