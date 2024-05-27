# # WAP a checkbox, button ,list ,label widgets to a Tkinter GUI window in Python.
# MINE ==> clicking on button will show Button is clicked
# import tkinter as tk
# from tkinter import messagebox

# def show():
#     messagebox.showinfo("Title", "Button is clicked")

# root = tk.Tk()
# root.geometry("300x300")
# root.title("Checkbox Example")

# # label widget
# label = tk.Label(root, text="This is a label")
# label.pack()

# # checkbox widget
# check_state = tk.BooleanVar()
# check = tk.Checkbutton(root, text='Choose', variable=check_state)
# check.pack()

# # button widget
# btn = tk.Button(root, text='Click me', command=show)
# btn.pack()

# # listbox widget
# lst = tk.Listbox(root)
# lst.insert(1, "Python")
# lst.insert(2, "Java")
# lst.insert(3, "C++")
# lst.insert(4, "Any other")
# lst.pack()

# root.mainloop()



'''
# KARAN'S ==> clicking on the button will show the selected items in the listbox and the state of the checkbox
import tkinter as tk
from tkinter import messagebox

def button_action():
    selected_items = listbox.curselection()
    selected_text = ", ".join([listbox.get(i) for i in selected_items])
    checkbox_state = "checked" if var.get() else "unchecked"
    messagebox.showinfo("Info", f"Checkbox is {checkbox_state}. Selected items: {selected_text}")

# Create the main window
root = tk.Tk()
root.title("Tkinter Widgets Example")

# Create a label
label = tk.Label(root, text="This is a label")
label.pack(pady=10)

# Create a checkbox
var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Check me", variable=var)
checkbox.pack(pady=10)

# Create a listbox
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox_items = ["Item 1", "Item 2", "Item 3", "Item 4"]
for item in listbox_items:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)

# Create a button
button = tk.Button(root, text="Click me", command=button_action)
button.pack(pady=10)

# Run the application
root.mainloop()
'''

# '''
# ARYAN'S  ==> clicking on end will close the window
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry("400x400")
root.title("Endsem Q2")
# Label
lbl = Label(root, text="Hello")
lbl.pack()
# Checkbox
var1 = IntVar()
var2 = IntVar()
c1 = Checkbutton(root, text='Male', variable=var1)
c2 = Checkbutton(root, text='Female', variable=var2)
c1.pack()
c2.pack()
# List
listbox = Listbox(root)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "Any other")
listbox.pack()
# Button
btn = Button(root, text="End", command=root.quit)
btn.pack()
root.mainloop()
# '''