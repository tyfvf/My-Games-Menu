from tkinter import *
from Games import Games


class Application(Games):
    def __init__(self):
        self.root = Tk()
        self.screen()
        self.frames()
        self.title()
        self.game_buttons()
        self.scrollbar()
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
        self.first_bt = Button(self.canvas, text='My first game', bg='#FAB353', activebackground='#FAB353', command=self.first)
        self.canvas.create_window(220, 20, window=self.first_bt)

        self.pong_bt = Button(self.canvas, text='Pong', bg='#FAB353', activebackground='#FAB353', command=self.pong)
        self.canvas.create_window(220, 60, window=self.pong_bt)


    def scrollbar(self):
        self.scroll = Scrollbar(self.frame2, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
