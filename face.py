import pygame
from itertools import cycle
import random
import math
import sys


PIXEL_SCALE = 20
DECAY_SIZE = 10

pygame.init()

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
        super().__init__()
        self.image = pygame.Surface((len(data[0]) * PIXEL_SCALE, len(data) * PIXEL_SCALE))
        x = y = 0
        random.seed(0)
        for row in data:
            for col in row:
                for i in range(PIXEL_SCALE):
                    for j in range(PIXEL_SCALE):
                        offset = self.get_offset(x*PIXEL_SCALE+i, y*PIXEL_SCALE+j, len(data[0]) * PIXEL_SCALE, len(data) * PIXEL_SCALE)
                        self.image.set_at((x*PIXEL_SCALE+i, y*PIXEL_SCALE+j), pygame.Color(self.retro_color([25, 26, 22], offset=offset)) if col == "O" else pygame.Color(self.retro_color([130, 220, 170],offset=offset)))
                x += 1
            y += 1
            x = 0
        screenSize = pygame.display.Info()
        self.image = pygame.transform.scale(self.image, (screenSize.current_w, screenSize.current_h))
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


def translation_expression(expression):
    print(expression)
    if expression == "be regular":
        return REGULAR
    if expression in ["be sad", "goodnight", "goodbye"]:
        return SAD
    if expression in ["be happy", "hi", "hello", "hi monkey"]:
        return HAPPY
    if expression in ["do you smell it", "are you even working?"]:
        return SUSPICIOUS
    if expression in ["play Dead Steve"]:
        return DEAD
    if expression == "oh my god":
        return SHOCKED
    if expression == "music":
        return MUSIC

    return QUESTION


def start_face(expressionsQueue):
    pygame.mouse.set_visible(0)
    screen = pygame.display.set_mode()
    timer = pygame.time.Clock()
    expressions = [REGULAR, QUESTION, SHOCKED, SUSPICIOUS, HAPPY, SAD]
    current = REGULAR
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                current = random.choice(expressions)
            if e.type == pygame.MOUSEBUTTONDOWN:
                current = SHOCKED
            if e.type == pygame.KEYUP or e.type == pygame.MOUSEBUTTONUP:
                current = REGULAR
            # if e.type == pygame.USEREVENT:
            #     current = next(expressions)

        if expressionsQueue.empty() is False:
            current = translation_expression(expressionsQueue.get())

        screen.blit(current.image, current.rect)
        timer.tick(60)
        pygame.display.update()
