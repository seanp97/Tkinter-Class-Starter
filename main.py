from tkinter import Tk, Label, Button
import tkinter as tk

class TkinterGUI:
    def __init__(self, winTitle, xSize, ySize, *args):
         self.window = tk.Tk()
         if args:
              self.window.configure(bg=args)
         self.window.geometry(f'{xSize}x{ySize}')
         self.window.title(winTitle)
         self.window.mainloop()
    
MyNewGUI = TkinterGUI("My GUI", 500, 250)