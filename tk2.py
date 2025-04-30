import tkinter as tk
from tkinter import *

window = tk.Tk() 
window.geometry("500x250")
window.title("ITCS103_BSIT1B")

var1 = IntVar()
var2 = IntVar()

cb1 = tk.Checkbutton(window, text="Basketball", variable=var1)
cb2 = tk.Checkbutton(window, text="Volleyball", variable=var2)
cb1.pack()
cb2.pack()




window.mainloop()