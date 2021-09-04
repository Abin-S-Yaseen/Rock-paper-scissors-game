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

