from tkinter import *
from math import *

root = Tk()
#root.iconbitmap('E:\Python Projects\Python GUIs\Calculator\Dtafalonso-Android-Lollipop-Calculator.ico')

root.title("Calculator")
entry = Entry(root,  font = "Calibri 40", width=20, borderwidth=3)
entry.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)

def button_plus():
    first_num = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_num)
    entry.delete(0, END)

def button_equal():
    second_num = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, float(f_num) + float(second_num))
    if math == "subtract":
        entry.insert(0, float(f_num) - float(second_num))
    if math == "multiply":
        entry.insert(0, float(f_num) * float(second_num))
    if math == "divide":
        entry.insert(0, float(f_num) / float(second_num))

def button_subtract():
    first_num = entry.get()
    global f_num
    global math
    math = "subtract"
    f_num = float(first_num)
    entry.delete(0, END)

def button_multiply():
    first_num = entry.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_num)
    entry.delete(0, END)

def button_divide():
    first_num = entry.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_num)
    entry.delete(0, END)

def button_square_root():
    first_num = entry.get()
    entry.delete(0, END)
    entry.insert(0, sqrt(float(first_num)))



def button_square():
    first_num = entry.get()
    entry.delete(0, END)
    entry.insert(0, float(first_num) * float(first_num))


but1 = Button(root, text="1", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(1))
but2 = Button(root, text="2", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(2))
but3 = Button(root, text="3", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(3))
but4 = Button(root, text="4", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(4))
but5 = Button(root, text="5", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(5))
but6 = Button(root, text="6", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(6))
but7 = Button(root, text="7", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(7))
but8 = Button(root, text="8", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(8))
but9 = Button(root, text="9", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(9))
but0 = Button(root, text="0", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click(0))
butplus = Button(root, text="+", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=button_plus)
butclear = Button(root, text="C", font = "Calibri 30", padx=50, pady=15, borderwidth=4, command=button_clear)
butequal = Button(root, text="=", font = "Calibri 30", padx=50, pady=15, borderwidth=4, command=button_equal)
butsubtract = Button(root, text="-", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=button_subtract)
butmultiply = Button(root, text="x", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=button_multiply)
butdivide = Button(root, text="/", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=button_divide)
butsqureroot = Button(root, text="sqrt", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=button_square_root)
butsquare = Button(root, text="^2", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=button_square)
butpoint = Button(root, text=".", font = "Calibri 30", padx=5, pady=15, borderwidth=4, command=lambda: button_click("."))


but1.grid(row=3, column=0, sticky = "nsew")
but2.grid(row=3, column=1, sticky = "nsew")
but3.grid(row=3, column=2, sticky = "nsew")

but4.grid(row=2, column=0, sticky = "nsew")
but5.grid(row=2, column=1, sticky = "nsew")
but6.grid(row=2, column=2, sticky = "nsew")

but7.grid(row=1, column=0, sticky = "nsew")
but8.grid(row=1, column=1, sticky = "nsew")
but9.grid(row=1, column=2, sticky = "nsew")

but0.grid(row=4, column=0, sticky = "nsew")
butplus.grid(row=5, column=0, sticky = "nsew")
butclear.grid(row=4, column=1, columnspan=2, sticky = "nsew")
butequal.grid(row=5, column=1, columnspan=2, sticky = "nsew")

butsubtract.grid(row=6, column=0, sticky = "nsew")
butmultiply.grid(row=6, column=1, sticky = "nsew")
butdivide.grid(row=6, column=2,  sticky = "nsew")

butsqureroot.grid(row=7, column=0,  sticky = "nsew")
butsquare.grid(row=7, column=1,  sticky = "nsew")
butpoint.grid(row=7, column=2,  sticky = "nsew")

root.mainloop()