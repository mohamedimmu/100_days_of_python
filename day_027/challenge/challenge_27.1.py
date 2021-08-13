import tkinter

window = tkinter.Tk()

window.title("My First GUI App")
window.geometry("500x300+10+20") # window.minsize(width=500, height=300)

lbl = tkinter.Label(text="New Label", font=("Helvetica", 40, "italic"))
lbl.pack()
tps = tkinter.Label(text="Type Something",font=("Helvetica", 40, "italic"))
tps.pack()


window.clicked = 0


def button_clicked():
    window.clicked += 1
    lbl.config(text=f"Button got clicked {window.clicked}")
    tps.config(text=f"{text_field.get()}")


btn = tkinter.Button(text="Click Me", command=button_clicked)
btn.pack()

text_field = tkinter.Entry(width=25, bd=10)
text_field.pack()

window.mainloop()
