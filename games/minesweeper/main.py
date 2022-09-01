from games.minesweeper.Game import Game
from games.minesweeper.Board import Board


size = (12, 12)
prob = 0.1
board = Board(size, prob)
screenSize = (800, 800)
game = Game(board, screenSize)
game.run()