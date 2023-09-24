import random
from tkinter import *

def play_game():
    c_choice = random.choice(['rock', 'paper', 'scissors'])
    l4.configure(text='Computer chooses ' + c_choice)
    
    h_choice = e1.get()
    l6.configure(text='Human chooses ' + h_choice)

    global count_h, count_c
    if ((h_choice == 'rock' and c_choice == 'scissors') or
        (h_choice == 'scissors' and c_choice == 'paper') or
        (h_choice == 'paper' and c_choice == 'rock')):
        l7.configure(text="Human wins")
        count_h += 1
    elif h_choice == c_choice:
        l7.configure(text="Draw")
    else:
        l7.configure(text="Computer wins")
        count_c += 1

    e1.delete(0, 'end')  # Clear the Entry widget

a = Tk()
a.title("Rock, Paper & Scissors")
a.configure(bg="black")
a.geometry("1200x1200")

count_h = 0
count_c = 0

l1 = Label(a, text="__________________________Rock...Paper...Scissors__________________________", font=("times new roman", 30), bg="black", fg="white")
l1.pack()
l2 = Label(a, text="Hey! Welcome to the game Let's begin...", font=("times new roman", 15), bg="black", fg="white")
l2.pack()

l3 = Label(a, text='The computer chooses ', font=("times new roman", 15), bg="black", fg="white")
l4 = Label(a, text="", font=("times new roman", 15), bg="black", fg="white")
l5 = Label(a, text='Human chooses ', font=("times new roman", 15), bg="black", fg="white")
l6 = Label(a, text="", font=("times new roman", 15), bg="black", fg="white")
l7 = Label(a, text="", font=("times new roman", 15), bg="black", fg="white")


l3.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()


l10 = Label(a, text="Do you want to play again?", font=("times new roman", 15), bg="black", fg="white")
l10.pack()
e1 = Entry(a, width=40)
e1.place(x=700, y=140)

play_button = Button(a, text="Play", command=play_game)
play_button.pack()

a.mainloop()
