import tkinter as tk
from tkinter.constants import E, SW

window = tk.Tk()

button1 = tk.Button(window, text="Ordinary button")
# button1["anchor"] = E
button1.pack()

button2 = tk.Button(window, text="Colorful button", font=("Arial", 12, "underline"))
# button2["anchor"] = SW
button2.pack()

button2.config(bg="#000000")
button2.config(fg="yellow")
button2.config(activeforeground="#FF0000")
button2.config(activebackground="green")


window.mainloop()
