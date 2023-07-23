import pygame
import os
from time import sleep

class Game():
    def __init__(self, board, screensize):
        self.board = board
        self.screensize = screensize
        self.pieceSize = self.screensize[0] // self.board.getSize()[1], self.screensize[1] // self.board.getSize()[0]
        self.loadImages()


    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screensize)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)

            self.draw()
            pygame.display.update()
            if self.board.getWon():
                sound = pygame.mixer.Sound('./resources/audio/minesweeper/win.wav')
                sound.play()
                sleep(3)
                pygame.quit()
        

    
    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]


    def loadImages(self):
        self.images = {}
        for fileName in os.listdir('./resources/graphics/minesweeper'):
            if not fileName.endswith('.png'):
                continue
            image = pygame.image.load(r'./resources/graphics/minesweeper/' + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split('.')[0]] = image


    def getImage(self, piece):
        string = None
        if piece.getClicked():
            string = 'bomb-at-clicked-block' if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = 'flag' if piece.getFlagged() else 'empty-block'

        return self.images[string]


    def handleClick(self, position, rightClick):
        if self.board.getLost():
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)