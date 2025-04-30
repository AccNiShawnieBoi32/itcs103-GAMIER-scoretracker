import tkinter as tk
from tkinter import *

window = tk.Tk() 
window.geometry("500x250")
window.title("ITCS103_BSIT1B")

canvas = tk.Canvas(window, width=100, height=100)
canvas.pack()

#Creating a Line
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)

canvas.create_line(0,y,canvas_width, y)



window.mainloop()