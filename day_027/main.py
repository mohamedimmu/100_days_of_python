# Project 27 - Mile To Kilometer Conversion

from tkinter import *


def miles_to_km():
    miles = float(miles_text_field.get())
    kilometer = round(1.60934 * miles, 2)
    lbl_result.config(text=kilometer)


# Window
window = Tk()
window.minsize(width=400, height=200)
window.title("Mile to Km Converter")

# Entry
miles_text_field = Entry(width=10)
miles_text_field.grid(column=1, row=0)
miles_text_field.focus()

# Labels
lbl_miles = Label(text="Miles")
lbl_miles.grid(column=2, row=0)

lbl_equalto = Label(text="is equal to")
lbl_equalto.grid(column=0, row=1)

lbl_result = Label(text="0")
lbl_result.grid(column=1, row=1)

lbl_km = Label(text="Km")
lbl_km.grid(column=2, row=1)

# Button
btn = Button(text="Calculate", command=miles_to_km)
btn.grid(column=1, row=2)

window.mainloop()
