import pygame
from random import randint

def grid():
    x = randint(0, 480)
    y = randint(0, 480)
    return (x // 20 * 20, y // 20 * 20)


def check_collisions():
    if snake[0][0] > 480:
        return False
    elif snake[0][0] < 0:
        return False
    elif snake[0][1] > 480:
        return False
    elif snake[0][1] < 0:
        return False
    else:
        for i in snake[1:]:
            if snake[0][0] == i[0] and snake[0][1] == i[1]:
                return False
        return True


pygame.init()
display = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont('Comic Sans', 64, True)

snake_surf = pygame.Surface((20, 20))
snake = [[20, 60], [20, 40], [10, 20]]

food_surf = pygame.Surface((20, 20))
food_surf.fill('red')
food_pos = grid()

y_velocity = 20
x_velocity = 0
game_active = True
score = 0

# Game over
retry = font.render('Retry?', True, 'Black')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and y_velocity != 20:
                    y_velocity = -20
                    x_velocity = 0
                if event.key == pygame.K_s and y_velocity != -20:
                    y_velocity = 20
                    x_velocity = 0
                if event.key == pygame.K_a and x_velocity != 20:
                    y_velocity = 0
                    x_velocity = -20
                if event.key == pygame.K_d and x_velocity != -20:
                    y_velocity = 0
                    x_velocity = 20
        else:
            retry_rect = retry.get_rect(center = (250, 250))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    snake = [[20, 60], [20, 40], [10, 20]]
                    y_velocity = 20
                    x_velocity = 0
                    game_active = True
                    food_pos = grid()
                    score = 0
            if event.type == pygame.MOUSEMOTION:
                if retry_rect.collidepoint(event.pos):
                    retry = font.render('Retry!', True, 'Black')
                    retry = pygame.transform.scale(retry, (300, 150))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    retry = font.render('Retry?', True, 'Black')
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    if game_active:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if food_pos[0] == snake[0][0] and food_pos[1] == snake[0][1]:
            food_pos = grid()
            snake.append((0,0))
            score += 1
      
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])
        snake[0] = (snake[0][0] + x_velocity, snake[0][1] + y_velocity)

        score_text = font.render(f'{score}', True, 'black')
        score_text_rect = score_text.get_rect(center = (250, 40))

        display.fill('#B6D4A8')
        display.blit(food_surf, food_pos)
        display.blit(score_text, score_text_rect)
        for pos in snake:
            display.blit(snake_surf, pos)

        game_active = check_collisions()
    else:
        display.fill('#B6D4A8')
        display.blit(score_text, score_text_rect)
        text = font.render('Game Over', True, 'Black')
        text_rect = text.get_rect(center = (250, 150))
        retry_rect = retry.get_rect(center = (250, 250))
        display.blit(text, text_rect)
        display.blit(retry, retry_rect)

    pygame.display.update()
    clock.tick(20)

pygame.quit()
