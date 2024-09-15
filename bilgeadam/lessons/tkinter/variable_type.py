# tkinterda 4 tur gözlemlenebilir değişlen vardır
# intVar: 0
# doubleVar: 0.0
# booleanVar: false
# stringVar: ""
import tkinter as tk


def r_observer(*args):
    print("okuma işlemi gerçekleşti.")


def w_observer(*args):
    print("yazma işlemi gerçekleşti")


dummy = tk.Tk()

variable = tk.StringVar()
variable.set("abc")


r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)

variable.set(variable.get() + "d")
variable.trace_vdelete("r", r_obsid)

variable.set(variable.get() + "e")
variable.trace_vdelete("w", w_obsid)

variable.set(variable.get() + "f")

print(variable.get())
