import tkinter as tk # import tkinter in Python 3. If using Python 2 change to: import Tkinter
from tkinter import ttk # Themed tkinter (Improves GUI look and feel)

class Window(tk.Tk): # Class window inherits from tk.Tk()
	def __init__(self, title="Window", Height=500, Width=500, resizable=True, centered=True): # Constructor
		super().__init__()
		self.title(title)
		self.height, self.width = Height, Width
		self.geometry(str(Height)+"x"+str(Width))
		if(not resizable): self.resizable(0,0)
		if(centered): self.centerWindow()
		self.bind("<Escape>", self.exit)

	def centerWindow(self): # Makes the window appears on the screen center
		screenWidth, screenHeight = self.winfo_screenwidth(), self.winfo_screenheight()
		x, y = int(screenWidth/2 - self.width/2), int(screenHeight/2 - self.height/2)
		self.geometry("+{}+{}".format(x, y))

	def exit(self, event):
		self.destroy()

	def run(self):
		self.mainloop()