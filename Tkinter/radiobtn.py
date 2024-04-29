import tkinter as tk
root = tk.Tk()

radio1 = tk.Radiobutton(root, text='Python', value=1)
radio1.grid(row=0, column=0)
radio2 = tk.Radiobutton(root, text='Java', value=2)
radio2.grid(row=1, column=0)
radio3 = tk.Radiobutton(root, text='C++', value=3)
radio3.grid(row=2, column=0)

root.mainloop()