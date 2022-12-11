from tkinter import *
from tkinter import ttk
root = Tk()
var1 = IntVar()
Checkbutton(root, text='iya', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(root, text='tidak', variable=var2).grid(row=1, sticky=W)
ttk.Button(root, text="submit").grid()
root.mainloop()
