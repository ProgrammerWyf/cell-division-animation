# coding:utf-8
import pygame as pg
import sys
import math
import random
'''class Chrome:
    #  f

num = input("欢迎使用细胞分裂演示器 \n 王毅凡 制作于2025.4 \n 染色体数量：")


def position(number, radius, point):
    length = (radius*2 - 10)/number
    center = []
    for i in range(0,number):
        center.append((point[0] - (radius - 5) + (i+0.5)*length, point[1]))
    return [length, center]'''

radius = 270
size = width, height = 800, 600
origin = width / 2, height / 2
length = 200    # position(num,radius,origin)[0]
# center = position(num,radius,origin)[1]
c = random.randint(0, 255)


def draw_sector(screen, color, center, length):
    a = pg.draw.circle(screen, color, center, 5)  # 着丝粒
    b = a.copy()
    p_list = [center]
    p_list2, p_list3, p_list4 = [], [], []
    center_of_arc1 = int(center[0] - 1.25 * length * math.sin(math.pi / 6)), int(center[1] - 1.25 * length * math.cos(\
        math.pi / 6))

    for angle in range(29, -1, -1):
        x = int(center_of_arc1[0] + 1.25 * length * math.sin(math.radians(angle)))
        y = int(center_of_arc1[1] + 1.25 * length * math.cos(math.radians(angle)))
        p_list.append((x, y))  # 第一段染色体弧绘制

    # 第二段染色体弧绘制
    center_of_arc2 = p_list[-1][0], p_list[-1][1] - 0.15 * length
    for angle2 in range(-1, 60):
        x = int(center_of_arc2[0] - 0.15 * length * math.sin(math.radians(angle2)))
        y = int(center_of_arc2[1] + 0.15 * length * math.cos(math.radians(angle2)))
        p_list.append((x, y))

    # 第三段染色体弧绘制
    center_of_arc3 = center_of_arc2[0], center_of_arc2[1] + 0.15 * length
    for angle2 in range(45, -1, -1):
        x = int(center_of_arc3[0] - 0.15 * length * math.sin(math.radians(angle2)))
        y = int(center_of_arc3[1] - 0.15 * length * math.cos(math.radians(angle2)))
        p_list.append((x, y))

    p_list.append(center)
    quarter1 = pg.draw.polygon(screen, color, p_list)

    for i in range(0, len(p_list)-1,):
        p_list2.append((origin[0]*2 - p_list[i][0], p_list[i][1]))
    quarter2 = pg.draw.polygon(screen, color, p_list2)

    for i in range(0, len(p_list)-1):
        p_list3.append((p_list[i][0],origin[1]*2-p_list[i][1]))
    quarter3 = pg.draw.polygon(screen, color, p_list3)

    for i in range(0, len(p_list) - 1):
        p_list4.append((origin[0] * 2-p_list[i][0], origin[1] * 2 - p_list[i][1]))
    quarter4 = pg.draw.polygon(screen, color, p_list4)

    return [quarter1, quarter2, quarter3, quarter4, ]

pg.init()
screen = pg.display.set_mode(size)
screen.fill('white')
pg.display.set_caption('Cell Division')
pg.draw.circle(screen, (0, 0, 0), origin, radius, width=1)   # 细胞膜
# for i in range(0, num - 1):
draw_sector(screen, (c, c, c), origin, length)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.update()
