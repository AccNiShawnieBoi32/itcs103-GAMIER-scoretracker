import tkinter as tk
from tkinter import ttk

windows = tk.Tk()
windows.title("Title man to nganiiii")
windows.geometry("1000x650")

Label = ttk.Label(master = windows, text = "Text man to nganiiii", font = "Arial 24")
Label.pack() 

windows.mainloop()