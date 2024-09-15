import tkinter as tk

window = tk.Tk()
window.title("my first tkinter app")
window.geometry("600x400")

label = tk.Label(window, text="hello tkinter!")
label.pack()


def on_button_click():
    label = tk.Label(window, text="button clicked")
    label.pack()


button = tk.Button(window, text="click me", command=on_button_click)
button.pack()

window.mainloop()
