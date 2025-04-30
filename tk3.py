import tkinter as tk
from tkinter import *

window = tk.Tk() 
window.geometry("500x250")
window.title("ITCS103_BSIT1B")


sex = IntVar()

rb1 = tk.Radiobutton(window, text="Male", variable=sex, value="male")
rb2 = tk.Radiobutton(window, text="Female", variable=sex, value="female")
rb1.pack()
rb2.pack()






window.mainloop()