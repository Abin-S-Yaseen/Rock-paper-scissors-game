# Rock Paper Scissors Game

import tkinter
from tkinter import *
import random
from PIL import ImageTk,Image

# Setting up the window
root = Tk()
root.geometry('900x650')
root.maxsize(900,650)
root.minsize(900,580)
root.configure(background='#9999FF')
root.title('Rock paper scissors')

# Initial score values
user_score = 0
sys_score = 0

# Main game execution function
def play_game(user_selection):
    
    # Choice of the computer
    choices = ['rock','paper','scissors']
    choice = random.choice(choices)

    global user_score
    global sys_score

    # Various conditions that happen in the game
    if user_selection == 'rock':

        if choice == 'rock':
            sys_rock_img.config(bg='white')
            sys_paper_img.config(bg='#9999FF')
            sys_scissors_img.config(bg='#9999FF')

        if choice == 'paper':
            sys_score += 1
            sys_rock_img.config(bg='#9999FF')
            sys_paper_img.config(bg='white')
            sys_scissors_img.config(bg='#9999FF')

        if choice == 'scissors':
            user_score += 1
            sys_rock_img.config(bg='#9999FF')
            sys_paper_img.config(bg='#9999FF')
            sys_scissors_img.config(bg='white')

        user_paper_img.config(bg='#9999FF')
        user_scissors_img.config(bg='#9999FF')
        user_rock_img.config(bg='white')


    if user_selection == 'paper':

        if choice == 'rock':
            user_score += 1
            sys_rock_img.config(bg='white')
            sys_paper_img.config(bg='#9999FF')
            sys_scissors_img.config(bg='#9999FF')

        if choice == 'paper':
            sys_rock_img.config(bg='#9999FF')
            sys_paper_img.config(bg='white')
            sys_scissors_img.config(bg='#9999FF')
        
        if choice == 'scissors':
            sys_score += 1
            sys_rock_img.config(bg='#9999FF')
            sys_paper_img.config(bg='#9999FF')
            sys_scissors_img.config(bg='white')

        user_rock_img.config(bg='#9999FF')
        user_scissors_img.config(bg='#9999FF')
        user_paper_img.config(bg='white')

    if user_selection == 'scissors':

        if choice == 'rock':
            sys_score += 1
            sys_rock_img.config(bg='white')
            sys_paper_img.config(bg='#9999FF')
            sys_scissors_img.config(bg='#9999FF')

        if choice == 'paper':
            user_score += 1
            sys_rock_img.config(bg='#9999FF')
            sys_paper_img.config(bg='white')
            sys_scissors_img.config(bg='#9999FF')

        if choice == 'scissors':
            sys_rock_img.config(bg='#9999FF')
            sys_paper_img.config(bg='#9999FF')
            sys_scissors_img.config(bg='white')

        user_rock_img.config(bg='#9999FF')
        user_paper_img.config(bg='#9999FF')
        user_scissors_img.config(bg='white')

    sys_score_value.configure(text=sys_score)
    user_score_value.configure(text=user_score)


# importing system images
sys_rock_image = ImageTk.PhotoImage(Image.open('Images/rock.png'))
sys_paper_image = ImageTk.PhotoImage(Image.open('Images/paper.png'))
sys_scissors_image = ImageTk.PhotoImage(Image.open('Images/scissors.png'))

# importing user images
user_rock_image = ImageTk.PhotoImage(Image.open('Images/rock-user.png'))
user_paper_image = ImageTk.PhotoImage(Image.open('Images/paper-user.png'))
user_scissors_image = ImageTk.PhotoImage(Image.open('Images/scissors-user.png'))

# showing system images on screen as Label
sys_rock_img = Label(root,image=sys_rock_image,bg='#9999FF',relief=GROOVE)
sys_rock_img.place(relx=0.05,rely=0.078)
sys_paper_img = Label(root,image=sys_paper_image,bg='#9999FF',relief=GROOVE)
sys_paper_img.place(relx=0.05,rely=0.381)
sys_scissors_img = Label(root,image=sys_scissors_image,bg='#9999FF',relief=GROOVE)
sys_scissors_img.place(relx=0.05,rely=0.686)

# showing user images on screen as Button
user_rock_img = Button(root,image=user_rock_image,bg='#9999FF',relief=GROOVE,command=lambda:play_game('rock'))
user_rock_img.place(relx=0.71,rely=0.078)
user_paper_img = Button(root,image=user_paper_image,bg='#9999FF',relief=GROOVE,command=lambda:play_game('paper'))
user_paper_img.place(relx=0.71,rely=0.381)
user_scissors_img = Button(root,image=user_scissors_image,bg='#9999FF',relief=GROOVE,command=lambda:play_game('scissors'))
user_scissors_img.place(relx=0.71,rely=0.686)

# showing other components on the screen
sys_label = Label(root,text='COMPUTER',font=('Courier',15,'bold'),bg='#9999FF',fg='white')
sys_label.place(relx=0.105,rely=0.03)
user_label = Label(root,text='YOU',font=('Courier',15,'bold'),bg='#9999FF',fg='white')
user_label.place(relx=0.8,rely=0.03)
score_head_label = Label(root,text='SCORE  BOARD',font=('Ubuntu',15),width=17,bg='white',relief=GROOVE)
score_head_label.place(relx=0.391,rely=0.425)
line = Label(root,text=('''
                          |
                          |
                          |
                          |
                          |
                          |
                          |
                          |
          '''),bg='#9999FF')
line.place(relx=0.408,rely=0.47)
sys_score_label = Label(root,text="COMP:",font=('Courier',14),bg='white',relief=GROOVE)
sys_score_label.place(relx=0.391,rely=0.5)
user_score_label = Label(root,text='YOU: ',font=('Courier',14),bg='white',relief=GROOVE)
user_score_label.place(relx=0.539,rely=0.5)
sys_score_value = Label(root,text=0,font=('Ubuntu',15),width=5,bg='white',relief=GROOVE)
sys_score_value.place(relx=0.391,rely=0.57)
user_score_value = Label(root,text=0,font=('Ubuntu',15),width=5,bg='white',relief=GROOVE)
user_score_value.place(relx=0.539,rely=0.57)
vs_label = Label(root,text='V/S',font=('helvetica',30),bg='#9999FF')
vs_label.place(relx=0.453,rely=0.25)


