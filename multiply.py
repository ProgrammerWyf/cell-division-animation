# coding:utf-8
import pygame as pg
import sys
import math
import random


class Chromosome:
    def __init__(self):  # 不要也罢？
        self.p_list = []
        self.p_list2 = []
        self.p_list3 = []
        self.p_list4 = []
        self.track = []
        self.track2 = []
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    @classmethod
    def position(cls, number, radius, length, point):
        center = []
        for i in range(0, number):
            center.append((point[0] - (radius - 5) + (i + 0.5) * length, point[1]))
        return center

    def draw_sector(self, center, length):
        self.p_list = [center]
        self.p_list2 = []
        self.p_list3 = []
        self.p_list4 = []

        center_of_arc1 = int(center[0] - 1.25 * length * math.sin(math.pi / 6)), int(center[1] - 1.25 * length * math.
                                                                                     cos(math.pi / 6))
        # 染色体绘制基础准备
        for angle in range(29, -1, -1):
            x = int(center_of_arc1[0] + 1.25 * length * math.sin(math.radians(angle)))
            y = int(center_of_arc1[1] + 1.25 * length * math.cos(math.radians(angle)))
            self.p_list.append((x, y))  # 第一段染色体弧绘制

        # 第二段染色体弧绘制
        center_of_arc2 = self.p_list[-1][0], self.p_list[-1][1] - 0.15 * length
        for angle2 in range(-1, 60):
            x = int(center_of_arc2[0] - 0.15 * length * math.sin(math.radians(angle2)))
            y = int(center_of_arc2[1] + 0.15 * length * math.cos(math.radians(angle2)))
            self.p_list.append((x, y))

        # 第三段染色体弧绘制
        center_of_arc3 = center_of_arc2[0], center_of_arc2[1] + 0.15 * length
        for angle2 in range(45, -1, -1):
            x = int(center_of_arc3[0] - 0.15 * length * math.sin(math.radians(angle2)))
            y = int(center_of_arc3[1] - 0.15 * length * math.cos(math.radians(angle2)))
            self.p_list.append((x, y))

        # 右下角染色体绘制
        for i in range(0, len(self.p_list)):
            self.p_list2.append((center[0] * 2 - self.p_list[i][0], self.p_list[i][1]))

        # 左上角
        for i in range(0, len(self.p_list)):
            self.p_list3.append((self.p_list[i][0], center[1] * 2 - self.p_list[i][1]))

        # 右上角
        for i in range(0, len(self.p_list)):
            self.p_list4.append((center[0] * 2 - self.p_list[i][0], center[1] * 2 - self.p_list[i][1]))

    def spindle(self, radius, number):
        for j in range(1, 245):
            new_length = int(math.sqrt((radius - 5) ** 2 - j ** 2))
            self.track.append((400 - new_length + (i + 0.5) * 2 * new_length / number, 300 - j))
            self.track2.append((400 - new_length + (i + 0.5) * 2 * new_length / number, 300 + j))

    def move(self, vect):
        for j in range(0, len(self.p_list)):
            self.p_list[j] = (self.p_list[j][0] + vect[0], self.p_list[j][1] - vect[1])
            self.p_list2[j] = (self.p_list2[j][0] + vect[0], self.p_list2[j][1] - vect[1])
            self.p_list3[j] = (self.p_list3[j][0] + vect[0], self.p_list3[j][1] + vect[1])
            self.p_list4[j] = (self.p_list4[j][0] + vect[0], self.p_list4[j][1] + vect[1])
        del self.track[0]
        del self.track2[0]


def movement():
    while move < len(chromosomes[0].track) - 1:
        screen.fill("white")
        pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((390, 35), (20, 10)))
        pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((396, 35), (8, 20)))  # 上中心粒
        pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((390, 565), (20, 10)))
        pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((396, 555), (8, 20)))  # 下中心粒
        pg.draw.rect(screen, (0, 0, 0), (130, 10, 540, 580), width=5, border_radius=1)  # 细胞膜
        for k in range(0, len(chromosomes)):
            vector = (chromosomes[k].track[move + 1][0] - chromosomes[k].track[move][0], chromosomes[k].track[move + 1]
            [1] - chromosomes[k].track[move][1])
            chromosomes[k].move(vector)
            pg.draw.polygon(screen, chromosomes[k].color, chromosomes[k].p_list)
            pg.draw.polygon(screen, chromosomes[k].color, chromosomes[k].p_list2)
            pg.draw.circle(screen, chromosomes[k].color, chromosomes[k].p_list[0], 5)
            pg.draw.polygon(screen, chromosomes[k].color, chromosomes[k].p_list3)
            pg.draw.polygon(screen, chromosomes[k].color, chromosomes[k].p_list4)
            pg.draw.circle(screen, chromosomes[k].color, chromosomes[k].p_list3[0], 5)
            pg.draw.aalines(screen, 'grey', False, chromosomes[k].track)
            pg.draw.aalines(screen, 'grey', False, chromosomes[k].track2)
        pg.display.update()
        pg.time.delay(20)


num = int(input("欢迎使用细胞分裂演示器\nversion 1.0 2025.4.27\n染色体数量："))
Radius = 270
size = width, height = 800, 600
origin = width / 2, height / 2
length = (Radius * 2 - 10) / num
Center = Chromosome.position(num, Radius, length, origin)

pg.init()
screen = pg.display.set_mode((800, 600))
screen.fill("white")

pg.display.set_caption('Cell Division')
chromosomes = []

pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((390, 35), (20, 10)))
pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((396, 35), (8, 20)))  # 上中心粒
pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((390, 565), (20, 10)))
pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((396, 555), (8, 20)))  # 下中心粒
pg.draw.rect(screen, (0, 0, 0), (130, 10, 540, 580), width=5, border_radius=1)  # 细胞膜
pg.draw.circle(screen, 'pink3', origin, Radius - 50)  # 细胞核

move = 2
key = 1

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            if key == 1:
                screen.fill('white')
                pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((390, 35), (20, 10)))
                pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((396, 35), (8, 20)))  # 上中心粒
                pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((390, 565), (20, 10)))
                pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((396, 555), (8, 20)))  # 下中心粒
                pg.draw.rect(screen, (0, 0, 0), (130, 10, 540, 580), width=5, border_radius=1)  # 细胞膜
                for i in range(0, len(Center)):
                    chromosomes.append(Chromosome())
                    chromosomes[i].draw_sector(Center[i], length / 2)
                    chromosomes[i].spindle(Radius, num)
                    pg.draw.circle(screen, chromosomes[i].color, Center[i], 5)
                    pg.draw.polygon(screen, chromosomes[i].color, chromosomes[i].p_list)
                    pg.draw.polygon(screen, chromosomes[i].color, chromosomes[i].p_list2)
                    pg.draw.polygon(screen, chromosomes[i].color, chromosomes[i].p_list3)
                    pg.draw.polygon(screen, chromosomes[i].color, chromosomes[i].p_list4)
                    pg.draw.aalines(screen, 'grey', False, chromosomes[i].track)
                    pg.draw.aalines(screen, 'grey', False, chromosomes[i].track2)
                pg.display.update()
                key += 1
            elif key == 2:
                movement()
                key += 1
            elif key == 3:
                for l in range(1, 270):
                    pg.draw.line(screen, 'black', (400 - l, 300), (400 + l, 300), width=10)
                    pg.display.update()
                    pg.time.delay(20)
                key += 1
            else:
                screen.fill('white')
                pg.draw.rect(screen, (0, 0, 0), (130, 10, 540, 290), width=5, border_radius=1)  # 细胞膜
                pg.draw.rect(screen, (0, 0, 0), (130, 300, 540, 290), width=5, border_radius=1)  # 细胞膜
                pg.draw.circle(screen, 'pink3', (400, 150), 100)
                pg.draw.circle(screen, 'pink3', (400, 445), 100)
    pg.display.update()
