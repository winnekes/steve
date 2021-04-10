import pygame
import random
import math


PIXEL_SCALE = 20
DECAY_SIZE = 10


class Expression(pygame.sprite.Sprite):
    def retro_color(self, color, variation=10, offset=0):
        return [max(0, min(255, x+random.randint(0, variation)+offset)) for x in color]

    def get_offset(self, x, y, width, height):
        offset = -DECAY_SIZE
        corner = False
        if x <= DECAY_SIZE:
            corner = True
            offset += x
        if x >= width - DECAY_SIZE:
            corner = True
            offset += width - x
        if y <= DECAY_SIZE:
            if corner:
                offset = -2*DECAY_SIZE + math.sqrt(x*x + y*y)
            else:
                offset += y
        if y >= height - DECAY_SIZE:
            if corner:
                offset = -2*DECAY_SIZE + math.sqrt(x*x + y*y)
            else:
                offset += height - y

        return 0 #min(offset*5,0) if x < DECAY_SIZE or y < DECAY_SIZE or x > width - DECAY_SIZE or y > height - DECAY_SIZE else 0

    def __init__(self, data):
        pygame.init()
        super().__init__()
        self.image = pygame.Surface((len(data[0]) * PIXEL_SCALE, len(data) * PIXEL_SCALE))
        x = y = 0
        random.seed(0)
        for row in data:
            for col in row:
                for i in range(PIXEL_SCALE):
                    for j in range(PIXEL_SCALE):
                        offset = self.get_offset(x*PIXEL_SCALE+i, y*PIXEL_SCALE+j, len(data) * PIXEL_SCALE, len(data) * PIXEL_SCALE)
                        if i == 0 or i == PIXEL_SCALE - 1 or j == 0 or j == PIXEL_SCALE - 1:
                            self.image.set_at((x*PIXEL_SCALE+i, y*PIXEL_SCALE+j), pygame.Color(self.retro_color([130, 220, 170],offset=7)))
                            continue
                        self.image.set_at((x*PIXEL_SCALE+i, y*PIXEL_SCALE+j), pygame.Color(self.retro_color([25, 26, 22], offset=offset)) if col == "O" else pygame.Color(self.retro_color([130, 220, 170],offset=offset)))
                x += 1
            y += 1
            x = 0
        screenSize = pygame.display.Info()
        self.image = pygame.transform.scale(self.image, (480, 320))
        self.rect = self.image.get_rect()



DEAD = Expression([
    "                     ",
    "                     ",
    "                     ",
    "   O   O     O   O   ",
    "    O O       O O    ",
    "     O         O     ",
    "    O O       O O    ",
    "   O   O     O   O   ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
])

MUSIC = Expression([
    "                     ",
    "                     ",
    "                     ",
    "       OOOOOOOOOO    ",
    "       OO     OO     ",
    "       OO     OO     ",
    "       OO     OO     ",
    "     OOOO   OOOO     ",
    "     OOO    OOO      ",
    "                     ",
    "                     ",
    "                     ",
])


REGULAR = Expression([
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "    OOOO     OOOO    ",
    "   OOOOOO   OOOOOO   ",
    "   OOOOOO   OOOOOO   ",
    "    OOOO     OOOO    ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
])

SHOCKED = Expression([
    "                     ",
    "                     ",
    "                     ",
    "    OOO       OOO    ",
    "   O   O     O   O   ",
    "   O   O     O   O   ",
    "   O   O     O   O   ",
    "   O   O     O   O   ",
    "    OOO       OOO    ",
    "                     ",
    "                     ",
    "                     ",
])

QUESTION = Expression([
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "    OOOO             ",
    "   OOOOOO    OOOO    ",
    "   OOOOOO   OOOOOO   ",
    "    OOOO     OOOO    ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
])


HAPPY = Expression([
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "    OOOO     OOOO    ",
    "   O    O   O    O   ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
])

SAD = Expression([
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "   OOOOOO   OOOOOO   ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
])


SUSPICIOUS = Expression([
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "   OOOOOO   OOOOOO   ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
])
