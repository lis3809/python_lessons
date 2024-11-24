import random

import pygame as pg

from lesson_24.mySuperSprite import MySuperSprite

pg.init()

# Высота и ширина окна
height: int = 600
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


def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img


# img = load_img('ingi.png')
# img1 = pg.transform.scale(img, (200, 200))
# img2 = pg.transform.scale(img, (700, 700))

all_sprites = pg.sprite.Group()
sprite = pg.sprite.Sprite()
sprite.image = load_img('ingi.png')
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)

img = load_img('ingi.png')
img = pg.transform.scale(img, (50, 50))

for i in range(100):
    # sprite = pg.sprite.Sprite(all_sprites)
    # sprite.image = img
    # sprite.rect = sprite.image.get_rect()
    # sprite.rect.x = random.randrange(width)
    # sprite.rect.y = random.randrange(height)
    my_sprite = MySuperSprite(all_sprites)

# Запускаем главный цикл
while True:

    """ Начало игровой логики  """
    # Обрабатываем события (мышки, клавиатуры...)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Закрашиваем фон
    window.fill(LIGHTGREEN)
    # window.blit(img, (0, 0))
    # window.blit(img1, (400, 50))
    # window.blit(img2, (0, 200))
    all_sprites.update()
    all_sprites.draw(window)

    # Различные игровые события

    """ Конец игровой логики  """
    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)
