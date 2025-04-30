import tkinter as tk
from tkinter import *

window = tk.Tk() 
window.geometry("500x250")
window.title("ITCS103_BSIT1B")


listbox = tk.Listbox(window)
listbox.insert(1, "Python")
listbox.insert(2, "HTML")
listbox.insert(3, "C#")
listbox.insert(4, "ASM")

listbox.pack()



window.mainloop()