from tkinter import *
from customtkinter import *
import awesometkinter as atk
from Games import Games


class Application(Games):
    def __init__(self):
        self.root = CTk()
        self.screen()
        self.frames()
        self.title()
        self.game_buttons()
        self.tooltips()
        self.root.mainloop()

    
    def screen(self):
        self.root.geometry('500x500')
        self.root.title('My Games Menu')
        self.root.resizable(False, False)


    def frames(self):
        self.frame1 = CTkFrame(self.root)
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.15)

        self.frame2 = CTkScrollableFrame(self.root)
        self.frame2.place(relx=0.05, rely=0.25, relwidth=0.90, relheight=0.70)


    def title(self):
        self.title_lb = CTkLabel(self.frame1, text='My Games Menu', font=('Times', 32, 'bold'))
        self.title_lb.pack(pady=20)

        self.note_lb = CTkLabel(self.frame1, text='on pygame', font=('Times', 9, 'bold'))
        self.note_lb.place(relx=0.85, rely=0.72)


    def game_buttons(self):
        self.first_bt = CTkButton(self.frame2, text='My first game',  command=self.first)
        self.first_bt.pack(pady=20)

        self.pong_bt = CTkButton(self.frame2, text='Pong', command=self.pong)
        self.pong_bt.pack()

        self.runner_bt = CTkButton(self.frame2, text='Runner',  command=self.runner)
        self.runner_bt.pack(pady=20)

        self.flappy_bt = CTkButton(self.frame2, text='Flappy Bird',   command=self.flappy)
        self.flappy_bt.pack()

        self.tic_bt = CTkButton(self.frame2, text='Tic Tac Toe',  command=self.tictactoe)
        self.tic_bt.pack(pady=20)

        self.snake_bt = CTkButton(self.frame2, text='Snake Game',  command=self.snake)
        self.snake_bt.pack()

        self.whip_bt = CTkButton(self.frame2, text='Whip Game',  command=self.whip)
        self.whip_bt.pack(pady=20)

        self.minesweeper_bt = CTkButton(self.frame2, text='Minesweeper',  command=self.minesweeper)
        self.minesweeper_bt.pack()

        self.chess_bt = CTkButton(self.frame2, text='Chess',  command=self.chess)
        self.chess_bt.pack(pady=20)

        self.tetris_bt = CTkButton(self.frame2, text='Tetris',  command=self.tetris)
        self.tetris_bt.pack()



    def tooltips(self):
        atk.tooltip(self.first_bt, 'This is the first game i made using pygame,\nwhile watching a 10 min casual video about')
        atk.tooltip(self.pong_bt, 'This is the game i made with the knowledge of that 10 min video')
        atk.tooltip(self.runner_bt, 'This is a game where i copied and learnt from one of the best channels about pygame, clear code,\nthe video was 3 hours and 47 min')
        atk.tooltip(self.flappy_bt, 'My first game after watching the clear code video,\ni already did a flappy bird clone in java so i had all sprites')
        atk.tooltip(self.tic_bt, 'Just practicing some logic and trying different styles of games')
        atk.tooltip(self.snake_bt, 'Same thing as the game above, pretty cool game')
        atk.tooltip(self.whip_bt, 'This i made with a self restriction time of one hour\nand under a random theme my friend chose, which was: whip')
        atk.tooltip(self.minesweeper_bt, 'A minesweeper clone OOP oriented, from a yt channel called Daniel Chang\nProps to him')
        atk.tooltip(self.chess_bt, 'A chees game OOP oriented, from a yt channel called Coding Spot\nProps to him')
        atk.tooltip(self.tetris_bt, 'A tetris game replica, pretty fun, props to Coder Space')
