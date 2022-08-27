from tkinter import *


class Application():
    def __init__(self):
        self.root = Tk()
        self.screen()
        self.frames()
        self.title()
        self.game_buttons()
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


    def title(self):
        self.title_lb = Label(self.frame1, text='My Games Menu', bg='#DE5E49', font=('Times', 32, 'bold'))
        self.title_lb.place(relx=0.13, rely=0.05, relheight=0.90)


    def game_buttons(self):
        self.first_bt = Button(self.frame2, text='My first game')
        self.first_bt.place(relx=0.4, rely=0.05)
