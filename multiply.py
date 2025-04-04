# coding:utf-8
import pygame as pg
import sys
import math

'''class Chrome:
    #  f '''

'''num = input("欢迎使用细胞分裂演示器 \n 王毅凡 制作于2025.4 \n 染色体数量：")
print num
'''
pg.init()
size = width, height = 800, 600
origin = width / 2, height / 2
screen = pg.display.set_mode(size)
pg.display.set_caption("sss")


def draw_sector(screen, color, center, length):
    pg.draw.circle(screen, color, center, 5)  # 着丝粒
    p_list = [center]

    center_of_arc1 = int(origin[0] - 1.25 * length * math.sin(math.pi / 6)), int(
        origin[1] - 1.25 * length * math.cos(math.pi / 6))
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

    pg.draw.polygon(screen, color, p_list)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        pg.draw.circle(screen, 255, origin, 270, width=1)
        draw_sector(screen, 100, origin, 200)
        pg.display.update()
