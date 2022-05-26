from tkinter import*
from tkinter.ttk import *
from time import strftime

top = Tk()
top.title("Clock By Lion Of Kurdistan")

def none():
    text = strftime(' %H:%M:%S %p ')
    lbl.config(text=text)
    lbl.after(1000,none)
lbl = Label(top,font=('digital-7',50,'bold'),
            background='black',foreground='red')
lbl.pack(anchor='center')
none()
mainloop()