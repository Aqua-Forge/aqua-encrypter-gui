import tkinter as tk
from tkinter import ttk
from tkWindow import *
import browsing as b
import os
import encrypt

def cryptography(mode):
	name = "Encrypt" if mode=="encrypt" else "Decrypt"
	encBox = Window(name, 400, 300, False, True)
	encBox.attributes("-topmost", True)
	defaultBg = encBox.cget('bg')

	menu = tk.Frame(encBox, width=400, height=300)
	menu.pack_propagate(0)
	menu.pack()

	title = tk.Label(menu, text=name, font=("times", 14, "bold"))
	title.pack(pady=10)

	txt1 = tk.Label(menu, text="File (.txt) path:")
	txt1.pack(padx=10, pady=5, anchor="w")

	pathFrame = tk.Frame(menu, width=400, height=30)
	pathFrame.pack_propagate(0)
	pathFrame.pack()

	def setEntry(entry, text):
		entry.delete(0, tk.END)
		entry.insert(0, text)

	def browse(entry, mode):
		encBox.attributes("-topmost", False)
		if(mode=="file"): setEntry(entry, b.browse_box())
		else: setEntry(entry, b.browse_folder())
		encBox.attributes("-topmost", True)

	pathEntry = tk.Entry(pathFrame, width=35)
	pathEntry.pack(padx=10, ipady=4, anchor="nw", side=tk.LEFT)

	browseButton = tk.Button(pathFrame, text="Browse", width=5, command=lambda:browse(pathEntry, "file"))
	browseButton.pack(anchor="ne", side=tk.LEFT)

	passFrame = tk.Frame(menu, width=400, height=60)
	passFrame.pack_propagate(0)
	passFrame.pack()

	txt2 = tk.Label(passFrame, text="Insert your key (password):")
	txt2.pack(padx=10, pady=5, anchor="w")

	passEntry = tk.Entry(passFrame, width=35, show='*')
	passEntry.pack(padx=10, ipady=4, anchor="nw", side=tk.LEFT)

	saveFrame = tk.Frame(menu, width=400, height=60)
	saveFrame.pack_propagate(0)
	saveFrame.pack()

	txt3 = tk.Label(saveFrame, text="Save in (select a folder):")
	txt3.pack(padx=10, pady=5, anchor="w")

	saveEntry = tk.Entry(saveFrame, width=35)
	saveEntry.pack(padx=10, ipady=4, anchor="nw", side=tk.LEFT)

	browseButton2 = tk.Button(saveFrame, text="Browse", width=5, command=lambda:browse(saveEntry, "folder"))
	browseButton2.pack(anchor="ne", side=tk.LEFT)

	buttonsFrame = tk.Frame(menu, width=400, height=60)
	buttonsFrame.pack_propagate(0)
	buttonsFrame.pack(pady=10, anchor="s")

	cancelButton = tk.Button(buttonsFrame, text="Cancel", width=10, command=lambda:encBox.destroy())
	cancelButton.pack(pady=10, padx=60, side=tk.LEFT)

	def crypt(mode): 
		filePath = pathEntry.get()
		key = passEntry.get()
		savePath = saveEntry.get()
		if(filePath=="" or not os.path.isfile(filePath)):
			txt1['text'] = "Invalid file path!"
			txt1['foreground'] = "red"
			return
		else:
			txt1.configure(text="File (.txt) path:")
			txt1.configure(foreground="black")
		if(key==""):
			txt2['text'] = "Please insert a key (password):"
			txt2['foreground'] = "red"
			return
		else:
			txt2.configure(text="Insert your key (password):")
			txt2.configure(foreground="black")
		if(savePath=="" or (not os.path.exists(savePath)) or os.path.isfile(savePath)):
			txt3['text'] = "Please insert a path to a folder:"
			txt3['foreground'] = "red"
			return
		else:
			txt3.configure(text="Save in (select a folder):")
			txt3.configure(foreground="black")

		if(mode=="encrypt"):
			encrypt.encryptFile(filePath, savePath+"/encrypted.txt", key)
		else: encrypt.decryptFile(filePath, savePath+"/decrypted.txt", key)

		sucess = Window("Sucess!", 250, 100, False, True)
		sucess.attributes("-topmost", True)
		modeMsg = "encrypted!" if mode=="encrypt" else "decrypted!"
		msg = tk.Label(sucess, text="Successfully " + modeMsg)
		msg.pack(pady=15)

		def quit():
			encBox.destroy()
			sucess.destroy()

		okBut = tk.Button(sucess, text="Ok", width=10, command=lambda:quit())
		okBut.pack()

		sucess.run()
		
	encButtonName = "Encrypt" if mode=="encrypt" else "Decrypt"
	encButton = tk.Button(buttonsFrame, text=encButtonName, width=10, command=lambda:crypt(mode))
	encButton.pack(pady=10, padx=20, side=tk.LEFT)

	encBox.run()

def howToUse():
		htu = Window("How to use", 300, 300, False, True)
		htuMenu = tk.Frame(htu, width=280, height=200, background="white", borderwidth=1, relief="solid")
		htuMenu.pack_propagate(0)
		htuMenu.pack(pady=20, padx=10, side=tk.TOP)
		htuText = tk.Frame(htuMenu, width=260, height=200, background="white")
		htuText.pack_propagate(0)
		htuText.pack(side=tk.LEFT)
		text = tk.Text(htuText, bg="white", wrap=tk.WORD)
		instr = "-> How the algorithm works:\n\n"
		instr += "The Text Encrypter can take an plain text (.txt) file and shuffle its characters, based on a passwod (key). "
		instr += "This \"encryption\" is based on shuffling characters and can't be easily broken. The reason for it is that the original text can only "
		instr += "be unscrambled with the same password used, and this isn't stored anywhere. "
		instr += "A brute force test would require to use an dictionary algorithm that "
		instr += "checks the words in every text file generated for each password test, being computationally very expensive "
		instr += "(practically not feasible)."
		instr += "\n\n~~~~~~~~~~~~~~~~~~~~\n\n"
		instr += "-> Encrypting and decrypting:\n\n"
		instr += "To encrypt a text file, just click on \"Encrypt\", select your file and give the password. "
		instr += "After that, an output encrypted text file will be generated in the desired location. "
		instr += "To decrypt an text, just click on \"Decrypt\", select the file generated, mentioned above, and give your password. "
		instr += "\n\n~~~~~~~~~~~~~~~~~~~~\n\n"
		instr += "-> Tips for safety:\n\n"
		instr += "Avoid forgetting the password, therefore it cannot be recovered, as well as the original text. "
		instr += "For make the almost impossible \"dictionary brute force\" even harder, you can also insert on your original "
		instr += "text some random characters, at random places in it. The longer your password is, the more secure "
		instr += "your encryption will be.\n\n"

		text.insert(tk.INSERT, instr)
		text.config(state=tk.DISABLED)
		text.pack()
		scrollb = tk.Scrollbar(htuMenu, command=text.yview, orient=tk.VERTICAL)
		scrollb.pack(side=tk.RIGHT, fill=tk.Y)
		text['yscrollcommand'] = scrollb.set
		okButton = tk.Button(htu, text="Ok", width=10, command=lambda:htu.destroy())
		okButton.bind("<Return>", lambda event:htu.destroy())
		okButton.focus()
		okButton.pack()
		htu.run()
