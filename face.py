import pygame
import random
import sys
import time

import expressions


def translation_expression(expression):
    print(expression)
    if expression == "be regular":
        return expressions.REGULAR
    if expression in ["be sad", "goodnight", "goodbye"]:
        return expressions.SAD
    if expression in ["be happy", "hi", "hello steve", "hi monkey"]:
        return expressions.HAPPY
    if expression in ["do you smell it", "are you even working?"]:
        return expressions.SUSPICIOUS
    if expression in ["play dead steve"]:
        return expressions.DEAD
    if expression == "oh my god":
        return expressions.SHOCKED
    if expression == "music":
        return expressions.MUSIC

    return expressions.QUESTION


def start_face(expressionsQueue):
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    screen = pygame.display.set_mode((480,320), pygame.FULLSCREEN)
    allExpressions = [expressions.REGULAR, expressions.QUESTION, expressions.SHOCKED, expressions.SUSPICIOUS, expressions.HAPPY, expressions.SAD]
    current = expressions.REGULAR

    while True:
        for e in pygame.event.get():
            print(e)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                current = random.choice(allExpressions)
            if e.type == pygame.MOUSEMOTION:
                current = expressions.SHOCKED
            if e.type == pygame.KEYUP or e.type == pygame.MOUSEBUTTONUP:
                current = expressions.REGULAR

        if expressionsQueue.empty() is False:
            current = translation_expression(expressionsQueue.get())

        timer = pygame.time.Clock()
        timer.tick()
        screen.blit(current.image, current.rect)
        pygame.display.update()
