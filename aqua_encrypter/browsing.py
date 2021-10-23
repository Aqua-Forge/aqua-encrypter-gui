import tkinter as tk
from tkinter import filedialog
import webbrowser as wb
import os

def browse_box():
    filePath = filedialog.askopenfilename(filetypes=(("Text File", "*.txt"),("All files", "*")))
    return filePath

def browse_folder():
    dirPath = filedialog.askdirectory()
    return dirPath

# def open(path):
#     full_path = "C:" if os.name=='nt' else "file://"
#     full_path += path
#     wb.open(full_path)

    # filePath = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    # if(filePath is None): return

# browse_box()
# open(folder_path)
# open("/home/data-hunter/Computação/Coding/GUI Coding/Python/Tkinter/Project")