import tkinter as tk
# terminalde --> pip install pillow
from PIL import Image, ImageTk

window = tk.Tk()

canvas = tk.Canvas(window, width=400, height=400, bg="yellow")
# canvas.create_line(0, 0, 200, 200,
#                    arrow=tk.BOTH, fill="red", smooth=True, width=3)

# canvas.create_rectangle(200,100,300,300, outline="white", width=5, fill="red")
# canvas.create_oval(100, 100, 300, 200, outline="red", width=20, fill="white")

image = Image.open("images/logo.png")
imaged_resized = image.resize((300, 140))
imagetk = ImageTk.PhotoImage(imaged_resized)

canvas.create_image(200, 200, image=imagetk)

button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)

window.mainloop()