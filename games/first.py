import pygame, sys

from pygame.locals import *
from random import randint

class Enemy:
    x_position = 0
    y_position = 0

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position


def main():
    pygame.init()

    clock = pygame.time.Clock()

    (width, height) = (640, 480)

    SQUARE_SIZE = 32
    DISPLAY = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game')

    blockTex = pygame.image.load('./games/graphics/square.png')

    font = pygame.font.SysFont('Times', 32)
    newfont = pygame.font.Font('./games/font/font.ttf', 64)

    x_position = width / 2 - SQUARE_SIZE / 2
    y_position = height / 2 - SQUARE_SIZE / 2

    score = 0

    enemies = []

    for i in range(10):
        enemies.append(Enemy(randint(0, width - 32), randint(-32, 32)))

    while True:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

        #

        keys = pygame.key.get_pressed()   # checking pressed keys
        if keys[pygame.K_d]:
            x_position += 3
        if keys[pygame.K_a]:
            x_position -= 3
        if keys[pygame.K_w]:
            y_position -= 3
        if keys[pygame.K_s]:
            y_position += 3

        for enemy in enemies:
            enemy.y_position += 3

            if enemy.y_position > 480:
                enemy.y_position = randint(-32, 32)
                enemy.x_position = randint(0, width - 32)
                score += 1

            if x_position + 32 > enemy.x_position and x_position < enemy.x_position + 32 and y_position + 32 > enemy.y_position and y_position < enemy.y_position + 32:
                x_position = width / 2 - SQUARE_SIZE / 2
                y_position = width / 2 - SQUARE_SIZE / 2
                score = 0

                enemies = []

                for i in range(5):
                    enemies.append(Enemy(randint(0, width - 32), randint(-32, 32)))


        DISPLAY.fill((255, 255, 255))
        DISPLAY.blit(blockTex, (x_position, y_position))

        for enemy in enemies:
            DISPLAY.blit(blockTex, (enemy.x_position, enemy.y_position))

        scoreText = newfont.render(f'{score}', True, 'black')
        DISPLAY.blit(scoreText, (DISPLAY.get_width() / 2, 0))

        #

        pygame.display.update()


main()
