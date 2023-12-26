''' Flash Card App Capstone '''
from tkinter import *
from random import choice
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Arial", 40, "italic")
FONT2 = ("Arial", 60, "bold")
try:
    words = pd.read_csv(r"ProjectsPerDay\Day 031\data\words_to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv(r"ProjectsPerDay\Day 031\data\french_words.csv")

to_learn = words.to_dict(orient="records")
word_chosen = {}

# -------------------------------------- SAVE THE PROGRESS --------------------------------------- #

def is_known():
    ''' Define if the word was correctly known '''
    global word_chosen
    to_learn.remove(word_chosen)
    words_to_learn = pd.DataFrame(to_learn)
    words_to_learn.to_csv("ProjectsPerDay\Day 031\data\english_words.csv", index=False)
    next_card()
    
# ---------------------------------------- FLIP THE CARDS ---------------------------------------- #

def flip_card():
    ''' Flip the Flash Card '''
    global word_chosen
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text=language2, fill="white")
    canvas.itemconfig(word, text=word_chosen[language2], fill="white")

# ------------------------------------ CREATE NEW FLASH CARDS ------------------------------------ #

def next_card():
    ''' Create a New Flash Card '''
    global word_chosen, flip_timer
    window.after_cancel(flip_timer)
    word_chosen = choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title, text=language1, fill="black")
    canvas.itemconfig(word, text=word_chosen[language1], fill="black")
    flip_timer = window.after(3000, func=flip_card)

# ------------------------------------------- UI SETUP ------------------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

language1 = list(words.columns.values)[0]
language2 = list(words.columns.values)[1]

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="ProjectsPerDay\Day 031\images\card_front.png")
card_back = PhotoImage(file="ProjectsPerDay\Day 031\images\card_back.png")
canvas_image = canvas.create_image(400, 263, image = card_front)
title = canvas.create_text(400, 150, text="", font= FONT1)
word = canvas.create_text(400, 263, text="", font= FONT2)
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file=r"ProjectsPerDay\Day 031\images\wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file=r"ProjectsPerDay\Day 031\images\right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
