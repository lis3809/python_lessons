import pygame as pg


class MySuperCircle:

    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        self.dir_h = 'right'
        self.width = 500

    def draw(self, win):
        pg.draw.circle(win, self.col, (self.x, self.y), self.rad)

    def move_by_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.y -= 10
        if keys[pg.K_DOWN]:
            self.y += 1
        if keys[pg.K_LEFT]:
            self.x -= 1
        if keys[pg.K_RIGHT]:
            self.x += 1

    def horizontal_movement(self):
        if self.dir_h == 'right':
            self.x += 1
            if self.x > self.width:
                self.dir_h = 'left'
        else:
            self.x -= 1
            if self.x < 0:
                self.dir_h = 'right'
