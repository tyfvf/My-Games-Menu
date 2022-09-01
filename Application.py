from tkinter import *
import awesometkinter as atk
from Games import Games


class Application(Games):
    def __init__(self):
        self.root = Tk()
        self.screen()
        self.frames()
        self.title()
        self.game_buttons()
        self.scrollbar()
        self.tooltips()
        self.root.mainloop()

    
    def screen(self):
        self.root.geometry('500x500')
        self.root.title('My Games Menu')
        self.root.resizable(False, False)
        self.root.config(bg='#F5895D')


    def frames(self):
        self.frame1 = Frame(self.root, bg='#DE5E49')
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.15)

        self.frame2 = Frame(self.root, bg='#DE5E49')
        self.frame2.place(relx=0.05, rely=0.25, relwidth=0.90, relheight=0.70)

        self.canvas = Canvas(self.frame2, bg='#DE5E49', scrollregion=(0, 0, 0, 700), height=500)


    def title(self):
        self.title_lb = Label(self.frame1, text='My Games Menu', bg='#DE5E49', font=('Times', 32, 'bold'))
        self.title_lb.place(relx=0.13, rely=0.05, relheight=0.90)

        self.note_lb = Label(self.frame1, text='on pygame', bg='#DE5E49', font=('Times', 9, 'bold'))
        self.note_lb.place(relx=0.85, rely=0.72)


    def game_buttons(self):
        self.first_bt = Button(self.canvas, text='My first game', width=12, bg='#FAB353', activebackground='#FAB353', command=self.first)
        self.canvas.create_window(220, 20, window=self.first_bt)

        self.pong_bt = Button(self.canvas, text='Pong', bg='#FAB353', width=12, activebackground='#FAB353', command=self.pong)
        self.canvas.create_window(220, 60, window=self.pong_bt)

        self.runner_bt = Button(self.canvas, text='Runner', bg='#FAB353', width=12, activebackground='#FAB353', command=self.runner)
        self.canvas.create_window(220, 100, window=self.runner_bt)

        self.flappy_bt = Button(self.canvas, text='Flappy Bird', bg='#FAB353',  width=12, activebackground='#FAB353', command=self.flappy)
        self.canvas.create_window(220, 140, window=self.flappy_bt)

        self.tic_bt = Button(self.canvas, text='Tic Tac Toe', bg='#FAB353', width=12, activebackground='#FAB353', command=self.tictactoe)
        self.canvas.create_window(220, 180, window=self.tic_bt)

        self.snake_bt = Button(self.canvas, text='Snake Game', bg='#FAB353', width=12, activebackground='#FAB353', command=self.snake)
        self.canvas.create_window(220, 220, window=self.snake_bt)

        self.whip_bt = Button(self.canvas, text='Whip Game', bg='#FAB353', width=12, activebackground='#FAB353', command=self.whip)
        self.canvas.create_window(220, 260, window=self.whip_bt)

        self.minesweeper_bt = Button(self.canvas, text='Minesweeper', bg='#FAB353', width=12, activebackground='#FAB353', command=self.minesweeper)
        self.canvas.create_window(220, 260, window=self.minesweeper_bt)


    def scrollbar(self):
        self.scroll = Scrollbar(self.frame2, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)


    def tooltips(self):
        atk.tooltip(self.first_bt, 'This is the first game i made using pygame,\nwhile watching a 10 min casual video about')
        atk.tooltip(self.pong_bt, 'This is the game i made with the knowledge of that 10 min video')
        atk.tooltip(self.runner_bt, 'This is a game where i copied and learnt from one of the best channels about pygame, clear code,\nthe video was 3 hours and 47 min')
        atk.tooltip(self.flappy_bt, 'My first game after watching the clear code video,\ni already did a flappy bird clone in java so i had all sprites')
        atk.tooltip(self.tic_bt, 'Just practicing some logic and trying different styles of games')
        atk.tooltip(self.snake_bt, 'Same thing as the game above, pretty cool game')
        atk.tooltip(self.whip_bt, 'This i made with a self restriction time of one hour\nand under a random theme my friend chose, which was: whip')
        atk.tooltip(self.minesweeper_bt, 'A minesweeper clone OOP oriented from a yt channel called Daniel Chang\nProps to him')
