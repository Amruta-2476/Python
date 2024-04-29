import tkinter as tk
root = tk.Tk()

check_state = tk.BooleanVar()
check_state.set(False)

check1 = tk.Checkbutton(root, text='Tea', var=check_state)
check1.grid(row=0, column=0)
check2 = tk.Checkbutton(root, text='Coffee', var=check_state)
check2.grid(row=1, column=0)
check3 = tk.Checkbutton(root, text='Water', var=check_state)
check3.grid(row=2, column=0)

root.mainloop()