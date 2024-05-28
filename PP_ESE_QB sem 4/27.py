# What will be the output of the following program?
from tkinter import *         # ==> import tkinter as tk
val = Tk()                    # ==> val = tk.Tk()
# val.title('Listbox') this is not there so title will be 'tk'
ch = Listbox(val)             # ==> ch = tk.Listbox(val)
ch.insert(1, 'Python')
ch.insert(2, 'C')
ch.insert(3, 'Java')
ch.insert(4, 'Any other')
ch.pack()
val.mainloop()

