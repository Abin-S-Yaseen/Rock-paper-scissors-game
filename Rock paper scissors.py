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
