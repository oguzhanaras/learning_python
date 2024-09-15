import tkinter as tk
from tkinter import font


def blink():
    global is_white
    if is_white:
        color = "black"
        label.config(fg="red")
    else:
        color = "white"
        label.config(fg="blue")
    is_white = not is_white
    frame.config(bg=color)
    frame.after(500, blink)


is_white = True

window = tk.Tk()

frame = tk.Frame(window, width=200, height=100, bg="yellow")
frame.pack()

my_font = font.Font(family="Helvetica", size=20, weight="bold")

label = tk.Label(frame, text="BilgeAdam", font=my_font)
label.pack()

frame.after(500, blink)

window.mainloop()
