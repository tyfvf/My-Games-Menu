class Games():

    def first(self):
        try:
            from games import first
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')

    
    def pong(self):
        try:
            from games import pong
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def runner(self):
        try:
            from games import runner
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def flappy(self):
        try:
            from games import flappybird
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def tictactoe(self):
        try:
            from games import tictactoe
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def snake(self):
        try:
            from games import snake
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def whip(self):
        try:
            from games import whip
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')
    
    
    def minesweeper(self):
        try:
            from games.minesweeper import main
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def chess(self):
        try:
            from games.chess import main
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')

    
    def tetris(self):
        try:
            from games import tetris
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')