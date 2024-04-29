# label  ==> single line text
# button
# checkbox
# entry  ==> input box
# combobox
# radiobutton
# menubar
# canvas ==> shapes
# frame ==> container

import tkinter as tk
root = tk.Tk()

root.title("Widgets")
l1 = tk.Label(root, text="Label text", font=("Arial", 40))
# l1.pack()
l1.grid(row=0, column=0)

b1 = tk.Button(root, text="Click me")
# b1.pack()  # cannot use pack and grid within the same master 'root'
b1.grid(row=1, column=1)
root.geometry("500x100")

root.mainloop()