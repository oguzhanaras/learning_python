import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(window, text="button 1")
button_2 = tk.Button(window, text="button 2")
button_3 = tk.Button(window, text="button 3")

button_1.pack(side=tk.RIGHT)
button_2.pack(side=tk.LEFT)
button_3.pack(side=tk.BOTTOM)


window.mainloop()