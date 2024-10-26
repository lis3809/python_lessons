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
object_to_draw = 'rect'
size_mark = 50

# Основное окно
window = pg.display.set_mode((width, hight))
# Закрашиваем фон
window.fill(WHITE)

# Запускаем главный цикл
while True:

    """ Начало игровой логики  """
    # Обрабатываем события (мышки, клавиатуры...)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEWHEEL:
            size_mark = size_mark + event.y
            print(size_mark)

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            object_to_draw = 'circle'
        elif keys[pg.K_q]:
            object_to_draw = 'rect'
        elif keys[pg.K_SPACE]:
            # Закрашиваем фон
            window.fill(WHITE)

    # Различные игровые события
    if object_to_draw == 'rect':
        pressed = pg.mouse.get_pressed()
        if pressed[0]:
            pos = pg.mouse.get_pos()
            pg.draw.rect(window, GRAY, (pos[0] - size_mark//2, pos[1] - size_mark//2, size_mark, size_mark))
    elif object_to_draw == 'circle':
        pressed = pg.mouse.get_pressed()
        if pressed[0]:
            pos = pg.mouse.get_pos()
            pg.draw.circle(window, BLACK, pos, size_mark)

    """ Конец игровой логики  """
    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)
