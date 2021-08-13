from tkinter import *

window = Tk()
window.title("Add")


def add(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


add_button = Button(text="add", command=lambda: add(5, 4, 5, 6, 7, 8, 9))
add_button.pack()

window.mainloop()
