# FRAME

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label")
label.pack()

frame = tk.Frame(window, height=300, width=300, bg="#033099")
frame.pack()

switch = tk.IntVar()
switch.set(1)

def on_off():
    if switch.get() == 0:
        switch.set(1)
    else:
        switch.set(0)


button = tk.Button(window, text="Button #1", command=on_off)
button.pack(fill=tk.X)


checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=40)
entry.pack()

choose = tk.IntVar()
choose.set(1)

raadio_button = tk.Radiobutton(window, text="Python", variable=choose, value=0)
raadio_button.pack()
raadio_button2 = tk.Radiobutton(window, text="JavaScript", variable=choose, value=1)
raadio_button2.pack()

listbox = tk.Listbox(window, height=4)
listbox.insert(1, "ankara")
listbox.insert(2, "istanbul")
listbox.insert(3, "trabzon")
listbox.pack()

scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

spinbox = tk.Spinbox(window, from_=0, to=50)
spinbox.pack()

message = tk.Message(window, text="this is a message")
message.pack()

window.mainloop()
