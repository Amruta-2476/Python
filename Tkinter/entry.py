import tkinter as tk
root = tk.Tk()

entry = tk.Entry(root)
entry.grid(row=0, column=0)

def submit():
    label2 = tk.Label(root, text=entry.get())   #to get the text in the entry input field
    label2.grid(row=2, column=1)

b1 = tk.Button(root, text="Submit", command=submit)
b1.grid(row=1, column=0)


root.mainloop()