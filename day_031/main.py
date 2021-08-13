# Project 31 - Flash Cards

from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')

to_learn = data.to_dict(orient="records")

current_card = {}


def next_word():
    global timer, current_card
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    timer = window.after(3000, show_translation)


def show_translation():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    next_word()
    df = pd.DataFrame(to_learn)
    df.to_csv('data/words_to_learn.csv', index=False)


# ------------------------------------------UI---------------------------------------------
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, show_translation)

# Images
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# Canva
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="English", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button
wrong_btn = Button(image=wrong_img, command=next_word)
wrong_btn.config(padx=50, pady=50)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_img, command=is_known)
right_btn.config(padx=50, pady=50)
right_btn.grid(column=1, row=1)

next_word()
window.mainloop()
