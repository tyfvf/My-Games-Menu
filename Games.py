import pygame

class Games():

    def first(self):
        try:
            from games_src.first import first
        except pygame.error:
            print('Suppressing pygame.quit() exception')

    
    def pong(self):
        try:
            from games_src.pong import pong
        except pygame.error:
            print('Suppressing pygame.quit() exception')


    def runner(self):
        try:
            from games_src.runner import runner
        except pygame.error:
            print('Suppressing pygame.quit() exception')


    def flappy(self):
        try:
            from games_src.flappybird import flappybird
        except pygame.error:
            print('Suppressing pygame.quit() exception')


    def tictactoe(self):
        try:
            from games_src.tictactoe import tictactoe
        except pygame.error:
            print('Suppressing pygame.quit() exception')


    def snake(self):
        try:
            from games_src.snake import snake
        except pygame.error:
            print('Suppressing pygame.quit() exception')


    def whip(self):
        try:
            from games_src.whipgame import whip
        except pygame.error:
            print('Suppressing pygame.quit() exception')
    
    
    def minesweeper(self):
        try:
            from games_src.minesweeper import main
        except pygame.error:
            print('Suppressing pygame.quit() exception')


    def chess(self):
        try:
            from games_src.chess import main
        except pygame.error:
            print('Suppressing pygame.quit() exception')

    
    def tetris(self):
        try:
            from games_src.tetris import tetris
        except pygame.error:
            print('Suppressing pygame.quit() exception')


    def space_invaders(self):
        try:
            from games_src.space_invaders import main
        except pygame.error:
            print('Suppressing pygame.quit() exception')
        