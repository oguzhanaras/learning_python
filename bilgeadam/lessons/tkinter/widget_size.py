import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text="Ordinary button")
button1.pack()

button2 = tk.Button(window, text="Exceptional button", font=("Arial", 12, "underline"))
button2.pack()

button2["borderwidth"] = 10
button2["highlightthickness"] = 10
button2["padx"] = 10
button2["pady"] = 25

window.mainloop()

