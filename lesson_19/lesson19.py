import pygame as pg

pg.init()


class Circle:
    def __init__(self, color, circle_radius, x, y, speed, jump_counter, is_jump):
        self.color = color
        self.circle_radius = circle_radius
        self.x = x
        self.y = y
        self.speed = speed
        self.jump_counter = jump_counter
        self.is_jump = is_jump

    def draw(self):
        pg.draw.circle(win, self.color, (self.x, self.y), self.circle_radius)

    def move_by_kyes(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.x += self.speed
        if keys[pg.K_UP]:
            self.y -= self.speed
        if keys[pg.K_DOWN]:
            self.y += self.speed

    def jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.is_jump = True
        if self.is_jump is True:
            if self.jump_counter >= -30:
                self.y -= self.jump_counter
                self.jump_counter -= 2
            else:
                self.jump_counter = 30
                self.is_jump = False


height = 500
wight = 500
x = 0
win = pg.display.set_mode((wight, height))
circle1 = Circle('yellow', 20, 250, 250, 2, 2, False)
circle100 = []
for i in range(100):
    a = Circle('red', 30, x, 150, 5, 7, False)
    circle100.append(a)
    x += 50
while True:
    win.fill((255, 255, 255))
    circle1.move_by_kyes()
    circle1.draw()
    circle1.jump()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    for i in circle100:
        i.draw()
        i.jump()
    pg.display.update()
    pg.time.delay(10)
