import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(window, width=200, height=100, bg="red")
frame2 = tk.Frame(window, width=200, height=100, bg="yellow")

button1 = tk.Button(frame1, text="Button 1 inside Frame 1")
button2 = tk.Button(frame1, text="Button 2 inside Frame 1")
button3 = tk.Button(frame2, text="Button 3 inside Frame 2")
button4 = tk.Button(frame2, text="Button 4 inside Frame 2")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

frame1.pack()
frame2.pack()

window.mainloop()