from tkinter import *

import random

screen=Tk()
screen.geometry("600x600")
screen.title("DICE ROLLER")

dice1=PhotoImage(file="Dice1.png")
dice2=PhotoImage(file="Dice2.png")
dice3=PhotoImage(file="Dice3.png")
dice4=PhotoImage(file="Dice4.png")
dice5=PhotoImage(file="Dice5.png")
dice6=PhotoImage(file="Dice6.png")

DICE=[dice1,dice2,dice3,dice4,dice5,dice6]

def roll():
    d=random.choice(DICE)
    t=Label(screen,image=d)
    t.place(x=100,y=20)

b=Button(screen,text="Roll Dice",font=("Arial",28),bg='pink',fg='blue',command=roll)
b.place(x=210,y=410)
