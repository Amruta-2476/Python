import tkinter as tk
root= tk.Tk()

root.title("My First GUI")
label = tk.Label(root, text="this is a label")
label.pack()   # pack is used to display the label on the window

root.mainloop()