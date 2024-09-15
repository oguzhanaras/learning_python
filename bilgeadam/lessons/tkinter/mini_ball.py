import tkinter as tk

# Pencere oluşturma
window = tk.Tk()
window.title("Top Hareket Ettirici")

# Canvas oluşturma
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Topu çizme
ball = canvas.create_oval(190, 190, 210, 210, fill="blue")


# Hareket fonksiyonu
def move_ball(event):
    if event.keysym == "Up":
        canvas.move(ball, 0, -10)  # Yukarı hareket
    elif event.keysym == "Down":
        canvas.move(ball, 0, 10)   # Aşağı hareket
    elif event.keysym == "Left":
        canvas.move(ball, -10, 0)  # Sola hareket
    elif event.keysym == "Right":
        canvas.move(ball, 10, 0)   # Sağa hareket


# Klavye olaylarını dinle
window.bind_all("<KeyPress-Up>", move_ball)
window.bind_all("<KeyPress-Down>", move_ball)
window.bind_all("<KeyPress-Left>", move_ball)
window.bind_all("<KeyPress-Right>", move_ball)

# Pencereyi çalıştırma
window.mainloop()
