import tkinter as tk
from tkinter import *

window = tk.Tk() 
window.geometry("500x250")
window.title("ITCS103_BSIT1B")

#Label
Label = tk.Label(window, text="Hello World!")
Label.pack()

#Button
button = tk.Button(window, text="DESTROY", width=25, command=window.destroy)
button.pack()




#input, Entry or Textbox
entry = tk.Entry(window)
entry.pack()

window.mainloop()