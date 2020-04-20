# Modules:
import tkinter as tk # import tkinter in Python 3. If using Python 2 change to: import Tkinter
from tkinter import ttk # Themed tkinter (Improves GUI look and feel)
import os, sys
# Personal modules:
from tkWindow import *
import functions as f

# Window features:
minWindowHeight, minWindowWidth = 500, 500
resizable = False
centered = True

# Program/Menu features:
iconImgPath = "Images/textlocker.gif"
programTitle = "Text Encrypter"
titleColor = "green"
bgColor = "white"
buttonWidth = 16
buttonColor = "palegreen"
buttonTextColor = "black"
footer = "Thelmo Pontes de Araujo"

def menu_1(window):
	# Main menu frame:
	menu = tk.Frame(window, width=480, height=480, background=bgColor, borderwidth=1, relief="solid")
	menu.pack_propagate(0) # Fix frame size
	menu.pack(padx=20, pady=20)

	# Texts, Frames and Images:
	title = tk.Label(menu, text=programTitle, fg=titleColor, font=("serif", 16, "bold", "italic"), background=bgColor)
	msg = tk.Label(menu, text=footer, fg="purple", background="white")
	buttons = tk.Frame(menu, width=200, height=280, background=bgColor)
	buttons.grid_propagate(0) # Fix frame size
	rightBox = tk.Frame(menu, width=200, height=300, background="white")
	rightBox.pack_propagate(0)
	# neuronImg = tk.PhotoImage(file='Images/textlocker.gif')
	# insertImg = tk.Label(rightBox, image=neuronImg, anchor="w", bg="black")
	# insertImg.neuronImg = neuronImg
	tipsText = tk.Frame(rightBox, width=200, height=130)
	tipsText.pack_propagate(0)
	tips = tk.Text(tipsText, wrap=tk.WORD, background="black", foreground="green2", font="fixedsys 10", borderwidth=0)
	tips.config(highlightbackground="black")

	tt="Hi there! Choose an option by clicking on it or pressing its number in keyboard. Thank you!"
	tips.insert(tk.INSERT, tt)
	tips.config(state=tk.DISABLED)
	tips.pack()
	def tipsTextEvent(event):
		tips.config(state=tk.NORMAL)
		if(event=='1'):
			tips.delete(1.0, tk.END)
			tips.insert(tk.INSERT, "Click here to encrypt (shuffle) a text file.")
		elif(event=='2'):
			tips.delete(1.0, tk.END)
			tips.insert(tk.INSERT, "Click here to decrypt a text file.")
		elif(event=='3'):
			tips.delete(1.0, tk.END)
			tips.insert(tk.INSERT, "Click here to see the software instructions.")
		elif(event=='4'):
			tips.delete(1.0, tk.END)
			tips.insert(tk.INSERT, "Click here to leave.")
		elif(event=='leave'):
			tips.delete(1.0, tk.END)
			tips.insert(tk.INSERT, tt)
		tips.config(state=tk.DISABLED)

	# Methods:
	def encrypt():
		return f.cryptography("encrypt")
	def decrypt():
		return f.cryptography("decrypt")
	def howToUse():
		return f.howToUse()
	def exit():
		window.destroy()

	def keyPress(event):
		if(event.char=='1'): encrypt()
		elif(event.char=='2'): decrypt()
		elif(event.char=='3'): howToUse()
		elif(event.char=='4'): exit()

	# Buttons:
	bt1 = tk.Button(buttons, text="1. Encrypt", fg=buttonTextColor, font="bold", width=buttonWidth, background=buttonColor, anchor="w", command=lambda:encrypt())
	bt1.bind("<Enter>", lambda event:tipsTextEvent("1"))
	bt1.bind("<Leave>", lambda event:tipsTextEvent("leave"))
	bt2 = tk.Button(buttons, text="2. Decrypt", fg=buttonTextColor, font="bold", width=buttonWidth, background=buttonColor, anchor="w", command=lambda:decrypt())
	bt2.bind("<Enter>", lambda event:tipsTextEvent("2"))
	bt2.bind("<Leave>", lambda event:tipsTextEvent("leave"))
	bt3 = tk.Button(buttons, text="3. How to use", fg=buttonTextColor, font="bold", width=buttonWidth, background=buttonColor, anchor="w", command=lambda:howToUse())
	bt3.bind("<Enter>", lambda event:tipsTextEvent("3"))
	bt3.bind("<Leave>", lambda event:tipsTextEvent("leave"))
	bt4 = tk.Button(buttons, text="4. Exit", fg="red3", font="bold", width=buttonWidth, background=buttonColor, anchor="w", command=lambda:exit())
	bt4.bind("<Enter>", lambda event:tipsTextEvent("4"))
	bt4.bind("<Leave>", lambda event:tipsTextEvent("leave"))
	window.bind("<KeyPress>", keyPress)
	
	# Visual:
	# window.iconphoto(True, tk.PhotoImage(file=iconImgPath)) # Disable for executable creation in Pyinstaller
	title.pack(pady=30, side=tk.TOP)
	buttons.pack(padx=15, pady=20, side=tk.LEFT, anchor="w")
	buttons.grid_rowconfigure(0)
	buttons.grid_columnconfigure(0, weight=1)
	bt1.grid(row=0, column=0, pady=13)
	bt2.grid(row=1, column=0, pady=13)
	bt3.grid(row=2, column=0, pady=13)
	bt4.grid(row=3, column=0, pady=13)
	rightBox.pack(padx=15, pady=10, anchor="e")
	# insertImg.pack()
	tipsText.pack(side=tk.LEFT)
	msg.pack(anchor=tk.SE, side=tk.BOTTOM)

def runApplication():
	window = Window(programTitle, minWindowHeight, minWindowWidth, resizable, centered)
	menu_1(window)
	window.run()
