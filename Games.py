class Games():

    def first(self):
        try:
            from games_src.first import first
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')

    
    def pong(self):
        try:
            from games_src.pong import pong
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def runner(self):
        try:
            from games_src.runner import runner
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def flappy(self):
        try:
            from games_src.flappybird import flappybird
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def tictactoe(self):
        try:
            from games_src.tictactoe import tictactoe
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def snake(self):
        try:
            from games_src.snake import snake
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def whip(self):
        try:
            from games_src.whipgame import whip
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')
    
    
    def minesweeper(self):
        try:
            from games_src.minesweeper import main
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')


    def chess(self):
        try:
            from games_src.chess import main
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')

    
    def tetris(self):
        try:
            from games_src.tetris import tetris
        except Exception:
            print('To execute only the game, without the menu, replace pygame.quit with exit()')