import tkinter as tk
root = tk.Tk()

label1 = tk.Label(root, text="Label text", underline=0)
label1.grid(row=0, column=0)

button1 = tk.Button(root, text="Click me", background="blue",foreground="white")
button1.grid(row=1, column=1)

root.mainloop()