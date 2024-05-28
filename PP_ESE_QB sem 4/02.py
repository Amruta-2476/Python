# # WAP a checkbox, button ,list ,label widgets to a Tkinter GUI window in Python.
# ==> clicking on button will show Button is clicked
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")
root.title("Checkbox, button ,list ,label")

def show():
    messagebox.showinfo("Title", "Button is clicked")

# label widget
label = tk.Label(root, text="This is a label")
label.pack()

# checkbox widget
check_state = tk.BooleanVar()
check = tk.Checkbutton(root, text='Choose', variable=check_state)
check2_state = tk.BooleanVar()
check2 = tk.Checkbutton(root, text='Choose 2', variable=check2_state)
check.pack()
check2.pack()

# button widget
btn = tk.Button(root, text='Click me', command=show)
btn.pack()

# listbox widget
lst = tk.Listbox(root)
lst.insert(1, "Python")
lst.insert(2, "Java")
lst.insert(3, "C++")
lst.insert(4, "Any other")
lst.pack()

root.mainloop()


# ==> clicking on end will close the window
# btn = Button(root, text="End", command=root.quit)
# btn.pack()
