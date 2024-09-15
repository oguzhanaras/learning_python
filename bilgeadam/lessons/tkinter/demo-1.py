import tkinter as tk
import time


def flash_lights():
    max_size = 200
    min_size = 50
    size = min_size
    grow = True

    for _ in range(50):
        if grow:
            size += 10
            if size >= max_size:
                grow = False
        else:
            size -= 10
            if size <= min_size:
                grow = True

        canvas.delete("circle")
        canvas.create_oval(
            (300 - size // 2, 200 - size // 2, 300 + size // 2, 200 + size // 2),
            fill="blue" if _ % 2 == 0 else "red", tags="circle"
        )
        skylight.update()
        time.sleep(0.1)


skylight = tk.Tk()
skylight.title("Police Lights")
skylight.geometry("600x600")

canvas = tk.Canvas(skylight, width=600, height=400)
canvas.pack()

button = tk.Button(skylight, text="Start Flashing!", command=flash_lights)
button.pack()

skylight.mainloop()


frame.after(500, blink)

window.mainloop()