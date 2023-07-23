import pygame

import pygame,sys
from pygame.locals import *
import random


def main():
    pygame.init()

    clock = pygame.time.Clock()

    WIDTH = 600
    HEIGHT = 400

    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pong Game')

    player1Tex = pygame.image.load('./resources/graphics/pong/player1.png')
    player2Tex = pygame.image.load('./resources/graphics/pong/player2.png')
    ballTex = pygame.image.load('./resources/graphics/pong/ball.png')

    font = pygame.font.SysFont('Times', 64)

    one_x_position = 0
    one_y_position = 0

    two_x_position = WIDTH - player2Tex.get_width()
    two_y_position = HEIGHT - player2Tex.get_height()

    ball_x_position = WIDTH / 2 - ballTex.get_width() / 2
    ball_y_position = HEIGHT / 2 - ballTex.get_height() / 2

    x_velocity = random.choice((-2, 2))
    y_velocity = random.choice((-2, 2))

    score1 = 0
    score2 = 0

    while True:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        # Move players
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            one_y_position -= 5
        if keys[pygame.K_s]:
            one_y_position += 5
        if keys[pygame.K_UP]:
            two_y_position -= 5
        if keys[pygame.K_DOWN]:
            two_y_position += 5

        # Check colisions
        if one_y_position + player1Tex.get_height() > HEIGHT:
            one_y_position = HEIGHT - player1Tex.get_height()
        if one_y_position < 0:
            one_y_position = 0
        if two_y_position + player2Tex.get_height() > HEIGHT:
            two_y_position = HEIGHT - player2Tex.get_height()
        if two_y_position < 0:
            two_y_position = 0

        # Move ball
        if ball_y_position + ballTex.get_height() > HEIGHT:
            y_velocity *= -1
        if ball_y_position < 0:
            y_velocity *= -1
        if ball_x_position + ballTex.get_width() > WIDTH - player2Tex.get_width() and ball_y_position >= two_y_position and ball_y_position <= two_y_position + player2Tex.get_height():
            x_velocity *= -1.2
            y_velocity *= 1.2
        if ball_x_position < player1Tex.get_width() and ball_y_position >= one_y_position and ball_y_position <= one_y_position + player1Tex.get_height():
            x_velocity *= -1.2
            y_velocity *= 1.2
        if ball_x_position + ballTex.get_width() > WIDTH:
            score1 += 1
            ball_x_position = WIDTH / 2 - ballTex.get_width() / 2
            ball_y_position = HEIGHT / 2 - ballTex.get_height() / 2
            x_velocity = random.choice((-2, 2))
            y_velocity = random.choice((-2, 2))
        if ball_x_position < 0:
            score2 += 1
            ball_x_position = WIDTH / 2 - ballTex.get_width() / 2
            ball_y_position = HEIGHT / 2 - ballTex.get_height() / 2
            x_velocity = random.choice((-2, 2))
            y_velocity = random.choice((-2, 2))
        
        ball_x_position += x_velocity
        ball_y_position += y_velocity

        DISPLAY.fill('white')
        DISPLAY.blit(player1Tex, (one_x_position, one_y_position))
        DISPLAY.blit(player2Tex, (two_x_position, two_y_position))
        DISPLAY.blit(ballTex, (ball_x_position, ball_y_position))

        score1Text = font.render(f'{score1}', True, 'red')
        score2Text = font.render(f'{score2}', True, 'blue')
        DISPLAY.blit(score1Text, (DISPLAY.get_width() / 2 - 64, 0))
        DISPLAY.blit(score2Text, (DISPLAY.get_width() / 2 + 64, 0))

        pygame.display.update()

main()