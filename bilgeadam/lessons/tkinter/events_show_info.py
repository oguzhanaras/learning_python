import tkinter as tk
from tkinter import messagebox


window = tk.Tk()


def clicked():
    messagebox.showinfo("info", "there are some info here\nthere are another one")


button1 = tk.Button(window, text="show info", command=clicked)
button1.pack()

button2 = tk.Button(window, text="quit", command=window.destroy)
button2.pack()

window.mainloop()
