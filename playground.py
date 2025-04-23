import pygame as pg
import sys
pg.init()
screen = pg.display.set_mode((800, 600))

pg.display.set_caption('Cell Division')
x = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    clock = pg.time.Clock()
    clock.tick(30)
    screen.fill('white')
    Quarter1 = pg.Surface((200, 200))
    Quarter1.fill('yellow')
    a = pg.draw.rect(Quarter1, (114, 114, 114), (390, 35, 2, 1))
    screen.blit(Quarter1,(x,13))
    x += 10
    if x > 800:
        x = 0
    pg.display.flip()
    pg.display.update()
    # pg.time.delay(1000)