import pygame as pg

pg.init()

# Высота и ширина окна
hight = 500
width = 500

FPS = 30
clock = pg.time.Clock()

# Различные переменные


# Основное окно
window = pg.display.set_mode((width, hight))

# Запускаем главный цикл
while True:
    # Закрашиваем фон
    window.fill('white')

    """ Начало игровой логики  """
    # Обрабатываем события (мышки, клавиатуры...)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


    # Различные игровые события






    """ Конец игровой логики  """
    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)
