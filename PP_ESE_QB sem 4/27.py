# What will be the output of the following program?
from tkinter import *
val = Tk()
ch = Listbox(val)
ch.insert(1, 'Python')
ch.insert(2, 'C')
ch.insert(3, 'Java')
ch.insert(4, 'Any other')
ch.pack()
val.mainloop()
