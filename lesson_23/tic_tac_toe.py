import pygame as pg

from lesson_23.board import Board

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
board = Board(width, height, 200)
# Запускаем главный цикл
while True:

    """ Начало игровой логики  """
    # Обрабатываем события (мышки, клавиатуры...)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)

    # Различные игровые события
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        board.clean_2()
    # if keys[pg.K_ESCAPE] or board.check_end:
    #     pg.quit()
    #     exit()

    # Закрашиваем фон
    window.fill(WHITE)
    board.render(window)

    """ Конец игровой логики  """
    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)
