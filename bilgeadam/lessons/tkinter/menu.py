import tkinter as tk
from tkinter import messagebox


def open_file():
    messagebox.showinfo("App", "This app does nothing")


def warn_file():
    messagebox.showwarning("Warning", "This is warning")


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)

sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)

sub_menu_file.add_command(label="Open", underline=0, command=open_file)
sub_menu_file.add_command(label="Warning", underline=0, command=warn_file)

main_menu.add_cascade(label="Edit", underline=0)
window.mainloop()