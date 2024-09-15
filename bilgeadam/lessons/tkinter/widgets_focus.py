import tkinter as tk


def flip_focus():
    if window.focus_get() is button1:
        button2.focus_set()
    else:
        button1.focus_set()
    window.after(1000, flip_focus)


window = tk.Tk()


button1 = tk.Button(window, text="first")
button1.pack()
button2 = tk.Button(window, text="second")
button2.pack()

window.after(2000, flip_focus)

window.mainloop()
