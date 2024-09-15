import tkinter as tk

window = tk.Tk()

button = tk.Button(
    window,
    text="button 1",
    bg="MediumPurple",
    fg="LightSalmon"
)

button.pack()

window.mainloop()