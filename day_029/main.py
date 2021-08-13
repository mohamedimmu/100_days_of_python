# Project 29 - Password Manager
# Resources - https://tkdocs.com/tutorial/firstexample.html

from tkinter import *
from tkinter import messagebox
import pyperclip as pc
from random import randint, choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def save():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []

    password_letters = [choice(letters) for _ in range(0, randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(0, randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(0, randint(2, 4))]
    password += password_letters + password_numbers + password_symbols

    shuffle(password)

    password = ''.join(password)
    password_text_field.insert(0, password)
    pc.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password_data():
    website = website_text_field.get()
    email = email_text_field.get()
    password = password_text_field.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \n "
                                                              f"Password: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data_text = f"{website} | {email} | {password} \n"
                data.write(data_text)

            website_text_field.delete(0, END)
            password_text_field.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canva = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=logo_img)
canva.grid(column=1, row=0)

# Labels
website_lbl = Label(text="Website: ")
website_lbl.grid(column=0, row=1)

email_lbl = Label(text="Email/Username: ")
email_lbl.grid(column=0, row=2)

password_lbl = Label(text="Password: ")
password_lbl.grid(column=0, row=3)

# Entry
website_text_field = Entry(width=51)
website_text_field.grid(column=1, row=1, columnspan=2)
website_text_field.focus()

email_text_field = Entry(width=51)
email_text_field.grid(column=1, row=2, columnspan=2)
email_text_field.insert(0, "defaultmail@gmail.com")

password_text_field = Entry(width=32)
password_text_field.grid(column=1, row=3)

# Buttons
generate_pw_button = Button(text="Generate Password", command=save)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=add_password_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
