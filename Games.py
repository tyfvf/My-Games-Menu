class Games():

    def first(self):
        try:
            from games import first
        except Exception:
            print('Just put sys.exit under pygame.quit')

    
    def pong(self):
        try:
            from games import pong
        except Exception:
            print('Just put sys.exit under pygame.quit')


    def runner(self):
        try:
            from games import runner
        except Exception:
            print('Just put sys.exit under pygame.quit')


    def flappy(self):
        try:
            from games import flappybird
        except Exception:
            print('Just put sys.exit under pygame.quit')


    def tictactoe(self):
        try:
            from games import tictactoe
        except Exception:
            print('Just put sys.exit under pygame.quit')


    def snake(self):
        try:
            from games import snake
        except Exception:
            print('Just put sys.exit under pygame.quit')


    def whip(self):
        try:
            from games import whip
        except Exception:
            print('Just put sys.exit under pygame.quit')
    
    
    def minesweeper(self):
        try:
            from games.minesweeper import main
        except Exception:
            print('Just put sys.exit under pygame.quit')


    def chess(self):
        try:
            from games.chess import main
        except Exception:
            print('Just put sys.exit under pygame.quit')