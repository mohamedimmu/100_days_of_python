# Grid Challenge

import tkinter as tk

# Creating the window
window = tk.Tk()
window.title("Grid Challenge")
window.minsize(width=500, height=300)

# Padding
window.config(padx=10, pady=10)

# Label
lbl = tk.Label(text="Grid Challenge")
lbl.grid(column=0, row=0)

# Button
btn1 = tk.Button(text="Button 1")
btn1.grid(column=2, row=0)


btn2 = tk.Button(text="Button 2")
btn2.grid(column=1, row=1)

# Entry
text_field = tk.Entry(width=10)
text_field.grid(column=3, row=2)

window.mainloop()