import random

import pygame as pg

def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img

class MySuperSprite(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_img('ingi.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(600)
        self.rect.y = random.randrange(600)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
