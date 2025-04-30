import tkinter as tk
from tkinter import *

window = tk.Tk() 
window.geometry("500x250")
window.title("ITCS103_BSIT1B")

menu = tk.Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(Label="File", menu=filemenu)

filemenu.add_command(Label="New")
filemenu.add_command(Label="Open")
filemenu.add_command(Label="Save")
filemenu.add_separator()
filemenu.add_command(Label="Exit", command=window.quit)

# editmenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editmenu)



window.mainloop()