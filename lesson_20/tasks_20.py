import random

import pygame as pg

from lesson_20.mySuperCircle import MySuperCircle

pg.init()

high = 500
width = 500

FPS = 30
clock = pg.time.Clock()

centr_x = width // 2
centr_y = high // 2
rad = 50

window = pg.display.set_mode((width, high))

list_circles = []
for i in range(100):
    list_circles.append(MySuperCircle(i * 10, i * 5, 30, random.choices(range(256), k=3)))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    window.fill('white')

    for circle in list_circles:
        circle.horizontal_movement()
        circle.draw(window)

    pg.display.update()
    clock.tick(FPS)
