import tkinter as tk


def mouse_over(event=None):
    button1["bg"] = "green"
    button1["fg"] = "white"


def mouse_out(event=None):
    button1["bg"] = "blue"
    button1["fg"] = "red"


window = tk.Tk()

button1 = tk.Button(window, text="enabled", bg="red", fg="yellow")
button1.bind("<Enter>", mouse_over)
button1.bind("<Leave>", mouse_out)
button1.pack()


window.mainloop()
