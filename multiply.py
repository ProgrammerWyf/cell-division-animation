# -*- coding:gbk -*-
import pygame as pg
import sys
import math
import random
from ctypes import windll


class Chromosome:
    def __init__(self, target_pos, color, length):
        self.p_list = []
        self.p_list2 = []
        self.p_list3 = []
        self.p_list4 = []
        self.track = []
        self.track2 = []
        self.color = color
        self.length = length

        self.start_pos = (random.randint(250, 450), random.randint(150, 450))
        self.current_pos = self.start_pos
        self.target_pos = target_pos
        self.move_progress = 0.0

    def draw_sector(self, center):
        self.p_list = [center]
        center_of_arc1 = int(center[0] - 1.25 * self.length * math.sin(math.pi / 6)), int(center[1] - 1.25 * self.length
                                                                                          * math.cos(math.pi / 6))
        # 染色体绘制基础准备
        for angle in range(29, -1, -1):
            x = int(center_of_arc1[0] + 1.25 * self.length * math.sin(math.radians(angle)))
            y = int(center_of_arc1[1] + 1.25 * self.length * math.cos(math.radians(angle)))
            self.p_list.append((x, y))  # 第一段染色体弧绘制

        # 第二段染色体弧绘制
        center_of_arc2 = self.p_list[-1][0], self.p_list[-1][1] - 0.15 * self.length
        for angle2 in range(-1, 60):
            x = int(center_of_arc2[0] - 0.15 * self.length * math.sin(math.radians(angle2)))
            y = int(center_of_arc2[1] + 0.15 * self.length * math.cos(math.radians(angle2)))
            self.p_list.append((x, y))

        # 第三段染色体弧绘制
        center_of_arc3 = center_of_arc2[0], center_of_arc2[1] + 0.15 * self.length
        for angle2 in range(45, -1, -1):
            x = int(center_of_arc3[0] - 0.15 * self.length * math.sin(math.radians(angle2)))
            y = int(center_of_arc3[1] - 0.15 * self.length * math.cos(math.radians(angle2)))
            self.p_list.append((x, y))

        # 右下角染色体绘制
        self.p_list2 = [(center[0] * 2 - self.p_list[i][0], self.p_list[i][1]) for i in range(0, len(self.p_list))]

        # 左上角:
        self.p_list3 = [(self.p_list[i][0], center[1] * 2 - self.p_list[i][1]) for i in range(0, len(self.p_list))]

        # 右上角
        self.p_list4 = [(center[0] * 2 - self.p_list[i][0], center[1] * 2 - self.p_list[i][1])
                        for i in range(0, len(self.p_list))]

    def spindle(self, radius, number, index):
        for j in range(1, 245):
            new_length = int(math.sqrt((radius - 5) ** 2 - j ** 2))
            x = 400 - new_length + (index + 0.5) * 2 * new_length / number
            self.track.append((x, 300 - j))
            self.track2.append((x, 300 + j))

    def move(self):  # 染色体整体移动
        if self.move_progress < 1.0:
            self.move_progress = min(1.0, self.move_progress + 0.02)
            t = self.move_progress
            x = self.start_pos[0] + (self.target_pos[0] - self.start_pos[0]) * t * t
            y = self.start_pos[1] + (self.target_pos[1] - self.start_pos[1]) * t*t
            self.current_pos = (int(x), int(y))
            self.draw_sector(self.current_pos)


def movement(chromosomes):
    for chrm in chromosomes:
        vx = chrm.track[1][0] - chrm.track[0][0]
        vy = chrm.track[1][1] - chrm.track[0][1]
        for p in range(len(chrm.p_list)):
            chrm.p_list[p] = (chrm.p_list[p][0] + vx, chrm.p_list[p][1] - vy)
            chrm.p_list2[p] = (chrm.p_list2[p][0] + vx, chrm.p_list2[p][1] - vy)
            chrm.p_list3[p] = (chrm.p_list3[p][0] + vx, chrm.p_list3[p][1] + vy)
            chrm.p_list4[p] = (chrm.p_list4[p][0] + vx, chrm.p_list4[p][1] + vy)
        del chrm.track[0], chrm.track2[0]


def position(number, radius, length, point):
    return [(point[0] - (radius - 5) + (i + 0.5) * length, point[1]) for i in xrange(number)]

Radius = 270
size = width, height = 800, 600
origin = width / 2, height / 2
Fade_speed = 3  # 常量声明


def main(num):
    move = False
    done = True
    key_stage = 0
    length = (Radius * 2 - 10) / (num * 2)
    Center = position(num*2, Radius, length, origin)
    chromosomes = []
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(num)] * 2
    lengths = [random.randint(-30, 30) + length for k in range(num)] * 2
    nucleus_alpha = 255

    l = 1
    kernel = (random.randint(350, 400), random.randint(140, 160))
    nucleus_surf = pg.Surface(size, pg.SRCALPHA)

    clock = pg.time.Clock()

    while True:
        screen.fill("white")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and done:
                if key_stage == 0:
                    chromosomes = [Chromosome(Center[q], colors[q], lengths[q] /2)
                                   for q in range(num*2)]
                    move = True
                    done = False
                    key_stage += 1
                else:
                    move = True
                    done = False
                    key_stage += 1

        if key_stage < 4:
            if move:
                if nucleus_alpha > 0:
                    nucleus_alpha = max(0, nucleus_alpha - Fade_speed)
                if key_stage == 1:
                    for index, chromo in enumerate(chromosomes):
                        chromo.draw_sector(chromo.current_pos)
                    done = True
                if key_stage == 2:
                    for idx, chromo in enumerate(chromosomes):
                        chromo.move()
                        if not chromo.track:
                            chromo.spindle(Radius, num*2, idx)
                        if chromo.move_progress == 1.0 and nucleus_alpha == 0:
                            move = False
                            done = True

                elif key_stage == 3:
                    movement(chromosomes)
                    for chromo in chromosomes:
                        pg.draw.aalines(screen, 'grey', False, chromo.track)
                        pg.draw.aalines(screen, 'grey', False, chromo.track2)
                    if len(chromosomes[0].track) <= 3:
                        move = False
                        done = True

            pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((390, 35), (20, 10)))
            pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((396, 35), (8, 20)))  # 上中心粒
            pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((390, 565), (20, 10)))
            pg.draw.ellipse(screen, (100, 100, 100), pg.Rect((396, 555), (8, 20)))  # 下中心粒
            pg.draw.rect(screen, (0, 0, 0), (130, 10, 540, 580), width=5, border_radius=5)  # 细胞膜
            pg.draw.circle(nucleus_surf, (205, 145, 158, nucleus_alpha), origin, Radius - 50)
            pg.draw.circle(nucleus_surf, (200, 155, 200, nucleus_alpha), (origin[0] - 60, origin[1] + 55), 100)
            screen.blit(nucleus_surf, (0, 0))
            for chromo in chromosomes:
                pg.draw.circle(screen, chromo.color, chromo.p_list[0], 5)
                pg.draw.polygon(screen, chromo.color, chromo.p_list)
                pg.draw.polygon(screen, chromo.color, chromo.p_list2)
                pg.draw.polygon(screen, chromo.color, chromo.p_list3)
                pg.draw.polygon(screen, chromo.color, chromo.p_list4)
                pg.draw.circle(screen, chromo.color, chromo.p_list3[0], 5)

        elif key_stage == 4:
            if move:
                pg.draw.line(screen, 'black', (400 - l, 300), (400 + l, 300), width=10)
                l += 1
                if nucleus_alpha < 255:
                    nucleus_alpha += Fade_speed
                if l == 270:
                    move = False
                    done = True
            else:
                pg.draw.line(screen, 'black', (130, 300), (670, 300), width=10)
            pg.draw.rect(screen, (0, 0, 0), (130, 10, 540, 580), width=5, border_radius=5)  # 细胞膜
            pg.draw.circle(nucleus_surf, (205, 145, 158, nucleus_alpha), (400, 155), (Radius - 50) / 2)
            pg.draw.circle(nucleus_surf, (205, 145, 158, nucleus_alpha), (400, 455), (Radius - 50) / 2)
            pg.draw.circle(nucleus_surf, (200, 155, 200, nucleus_alpha), kernel, 40)
            pg.draw.circle(nucleus_surf, (200, 155, 200, nucleus_alpha), (kernel[0], kernel[1] + 300), 40)
            screen.blit(nucleus_surf, (0, 0))

        else:
            pg.draw.rect(screen, (0, 0, 0), (130, 10, 540, 290), width=5, border_top_left_radius=5,
                         border_top_right_radius=5)
            pg.draw.rect(screen, (0, 0, 0), (130, 300, 540, 290), width=5, border_bottom_left_radius=5,
                         border_bottom_right_radius=5)
            pg.draw.circle(nucleus_surf, (205, 145, 158, nucleus_alpha), (400, 155), (Radius - 50) / 2)
            pg.draw.circle(nucleus_surf, (205, 145, 158, nucleus_alpha), (400, 455), (Radius - 50) / 2)
            pg.draw.circle(nucleus_surf, (200, 155, 200, nucleus_alpha), kernel, 40)
            pg.draw.circle(nucleus_surf, (200, 155, 200, nucleus_alpha), (kernel[0], kernel[1] + 300), 40)
            screen.blit(nucleus_surf, (0, 0))

        pg.display.flip()
        clock.tick(25)

if __name__ == '__main__':
    num = int(input("欢迎使用细胞分裂演示器\nversion 1.0 2025.5.13\n染色体对数："))
    pg.init()
    screen = pg.display.set_mode((800, 600))
    SetWindowPos = windll.user32.SetWindowPos
    SetWindowPos(pg.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 0x0001)
    pg.display.set_caption('Cell Division')
    main(num)
