import pygame
from sys import exit

def main():
    pygame.init()
    display = pygame.display.set_mode((300, 400))
    pygame.display.set_caption('Tic Tac Toe')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Comic Sans', 48, True)
    font_turn = pygame.font.SysFont('Comic Sans', 12, True)
    x_turn = True
    winner = False
    draw = False

    # Background
    display.fill('white')

    # Title
    title_surf = font.render('Tic Tac Toe', True, 'black', 'white')
    title_rect = title_surf.get_rect(center = (150, 40))
    
    # Game Over
    restart = font.render('Restart?', True, 'black', 'white')

    # Players
    x_surf = pygame.image.load('./resources/graphics/tictactoe/x.png')
    o_surf = pygame.image.load('./resources/graphics/tictactoe/o.png')

    # Tiles
    tiles = [
        x_surf.get_rect(topleft = (0, 100)), x_surf.get_rect(topleft = (100, 100)), x_surf.get_rect(topleft = (200, 100)),
        x_surf.get_rect(topleft = (0, 200)), x_surf.get_rect(topleft = (100, 200)), x_surf.get_rect(topleft = (200, 200)),
        x_surf.get_rect(topleft = (0, 300)), x_surf.get_rect(topleft = (100, 300)), x_surf.get_rect(topleft = (200, 300))
    ]

    positions = [
        False, False, False,
        False, False, False,
        False, False, False
    ]

    positionsX = [
        False, False, False,
        False, False, False,
        False, False, False
    ]

    positionsO = [
        False, False, False,
        False, False, False,
        False, False, False
    ]

    def check_draw():
        filled_tiles = 0
        for i in positions:
            if i:
                filled_tiles += 1

        if not winner and filled_tiles == 9:
            return True
        else:
            return False


    def check_winner():
        if positionsX[0] and positionsX[1] and positionsX[2]:
            return True
        elif positionsX[0] and positionsX[4] and positionsX[8]:
            return True
        elif positionsX[0] and positionsX[3] and positionsX[6]:
            return True
        elif positionsX[3] and positionsX[4] and positionsX[5]:
            return True
        elif positionsX[6] and positionsX[7] and positionsX[8]:
            return True
        elif positionsX[1] and positionsX[4] and positionsX[7]:
            return True
        elif positionsX[2] and positionsX[5] and positionsX[8]:
            return True
        elif positionsX[2] and positionsX[4] and positionsX[6]:
            return True
        elif positionsO[0] and positionsO[1] and positionsO[2]:
            return True
        elif positionsO[0] and positionsO[4] and positionsO[8]:
            return True
        elif positionsO[0] and positionsO[3] and positionsO[6]:
            return True
        elif positionsO[3] and positionsO[4] and positionsO[5]:
            return True
        elif positionsO[6] and positionsO[7] and positionsO[8]:
            return True
        elif positionsO[1] and positionsO[4] and positionsO[7]:
            return True
        elif positionsO[2] and positionsO[5] and positionsO[8]:
            return True
        elif positionsO[2] and positionsO[4] and positionsO[6]:
            return True
        else:
            return False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if not winner and not draw:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    count = 0
                    for i in tiles:
                        if i.collidepoint(event.pos):
                            if x_turn:
                                if not positions[count]:
                                    display.blit(x_surf, i)
                                    x_turn = False
                                    positions[count] = True
                                    positionsX[count] = True
                            else:
                                if not positions[count]:
                                    display.blit(o_surf, i)
                                    x_turn = True
                                    positions[count] = True
                                    positionsO[count] = True

                        count += 1
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rect.collidepoint(event.pos):
                        display.fill('white')
                        winner = False
                        draw = False
                        x_turn = True
                        for i in range(0, 9):
                            positions[i] = False
                            positionsX[i] = False
                            positionsO[i] = False
                if event.type == pygame.MOUSEMOTION:
                    if restart_rect.collidepoint(event.pos):
                        restart = font.render('Restart!', True, 'Black')
                        restart = pygame.transform.scale(restart, (220, 100))
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    else:
                        restart = font.render('Restart?', True, 'Black')
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if not winner and not draw:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            # Title Display
            display.blit(title_surf, title_rect)

            if x_turn:
                turn = font_turn.render('X turn', True, 'black', 'white')
                display.blit(turn, (250, 80))
            else:
                turn = font_turn.render('O turn', True, 'black', 'white')
                display.blit(turn, (250, 80))

            # Drawing lines
            pygame.draw.line(display, 'black', (100, 100), (100, 400), 5)
            pygame.draw.line(display, 'black', (200, 100), (200, 400), 5)

            pygame.draw.line(display, 'black', (0, 200), (300, 200), 5)
            pygame.draw.line(display, 'black', (0, 300), (300, 300), 5)

            winner = check_winner()
            draw = check_draw()
        else:
            if draw:
                text = font.render('DRAW!', True, 'Black', 'white')
            elif not x_turn:
                text = font.render('X WINS!!!', True, 'Black', 'white')
            else:
                text = font.render('O WINS!!!', True, 'Black', 'white')
            
            restart_rect = restart.get_rect(topleft = (50, 170))
            display.fill('white')
            display.blit(text, (50, 100))
            display.blit(restart, restart_rect)

        pygame.display.update()
        clock.tick(60)


main()