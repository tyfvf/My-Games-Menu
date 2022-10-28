class Games():

    def first(self):
        from games import first
        

    
    def pong(self):
        from games import pong
        


    def runner(self):
        from games import runner


    def flappy(self):
        from games import flappybird
        


    def tictactoe(self):
        from games import tictactoe
        


    def snake(self):
        from games import snake
        


    def whip(self):
        from games import whip
        
    
    
    def minesweeper(self):
        try:
            from games.minesweeper import main
        except Exception:
            print('Just put sys.exit under pygame.quit')