import tkinter as tk
from tkinter import messagebox


def show():
    text = f"Yiyecek: {radio1_var.get()}\nİçecek: {radio2_var.get()}"
    messagebox.showinfo("Seçimleriniz:", text)


window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window, text="Yiyecek seçiniz:")
label1.pack()

radio1_var = tk.IntVar()

radio1_1 = tk.Radiobutton(window, text="Pizza", variable=radio1_var, value=1)
radio1_1.select()
radio1_1.pack()

radio1_2 = tk.Radiobutton(window, text="Lahmacun", variable=radio1_var, value=2)
radio1_2.pack()

label2 = tk.Label(window, text="İçecek seçiniz:")
label2.pack()

radio2_var = tk.IntVar()

radio2_1 = tk.Radiobutton(window, text="Ayran", variable=radio2_var, value=1)
radio2_1.pack()

radio2_2 = tk.Radiobutton(window, text="Kola", variable=radio2_var, value=2)
radio2_2.select()
radio2_2.pack()

button = tk.Button(window, text="Seçimleri göster", command=show)
button.pack()

window.mainloop()