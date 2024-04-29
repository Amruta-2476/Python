import tkinter as tk
root = tk.Tk()

label1 = tk.Label(root, text="Label text", underline=0)
label1.grid(row=0, column=0)

def clicked():
    # print("Button was clicked")
    label2 = tk.Label(root, text="Button was clicked")
    label2.grid(row=2, column=1)

def changeLabel1Onclick():
    label1.configure(text="Button was clicked changed label1")

button1 = tk.Button(root, text="Click me", command=clicked)
# button1 = tk.Button(root, text="Click me", command=changeLabel1Onclick)
button1.grid(row=1, column=1)

root.mainloop()