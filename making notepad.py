from tkinter.filedialog import *
import tkinter as tk
 
canvas = tk.Tk()
canvas. geometry("400x600")
canvas.title("Notepad")
canvas.config(bg ="white")
top = Frame(canvas)
top.pack(padx=10,pady = 5, anchor ='nw')

b1 =Button(canvas,text="Open",bg= "white")
b1.pack(in_ = top ,side=LEFT)


b2= Button(canvas,text="Sava" ,bg= "white")
b2.pack(in_ = top ,side=LEFT)

canvas.mainloop()
