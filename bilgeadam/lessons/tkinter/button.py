import tkinter as tk

skylight = tk.Tk()

skylight.title("Skylight")

button = tk.Button(skylight, text="Bye!")
# button.pack()
button.place(x=50, y=100)

button2 = tk.Button(skylight, text="Hello!")
button2.place(x=100, y=50)

skylight.mainloop()
