import tkinter as tk
from tkinter import messagebox


def click(event=None):
    tk.messagebox.showinfo("Click", "I love clicks")


def click_right(event=None):
    tk.messagebox.showinfo("Click Right", "I clicked right")


def hover(event=None):
    radiobutton = tk.Label(window, text="Hovered")
    radiobutton.pack()


window = tk.Tk()

label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)   # label: widget,   event,   function
label.bind("<Button-3>", click_right)
label.pack()

button = tk.Button(window, text="Button")
button.bind("<Enter>", hover)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.pack()

window.mainloop()
