# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:30:08 2018

@author: Raunak
"""

from tkinter import *
import time
from PIL import Image, ImageTk

class Window(Frame):
    
    def __init__(self, master = None):
        
        Frame.__init__(self, master)
        
        self.master = master
        
        self.init_window()
        
    
    def init_window(self):
        
        self.master.title("GUI")
        
        self.pack(fill = BOTH, expand = 1)
        
        quitButton = Button(self, text = "Quit", command = self.client_exit)
        
        quitButton.place(x=0, y=0)
        
        #or quitButton.grid(row=0, column=0)
        
        #Making menu
        
        menu = Menu(self.master)
        self.master.config(menu = menu)
        
        file = Menu(menu)
        
        file.add_command(label = "Save")
        file.add_command(label = "Exit", command = self.client_exit)
        
        menu.add_cascade(label = 'File', menu=file)
        
        edit = Menu(menu)
        edit.add_command(label = "Show Image", command = self.showImage)
        
        edit.add_command(label = "Show Text", command = self.showText)
        
        menu.add_cascade(label = 'Edit', menu=edit)
        
        
        
        
        
    def client_exit(self):
        
        print("QUITTING...")
        
        time.sleep(2)
        
        root.destroy()
        
        #or self.master.destroy()
    

    def showImage(self):
        
        load = Image.open("D://study material//[FreeTutorials.Us] master-computer-vision-with-opencv-in-python//OpenCV-with-Python-master//images//Trump.jpg")
        render = ImageTk.PhotoImage(load)
        
        img = Label(self, image = render)
        img.image = render
        img.place(x=5, y=5)
        
    
    def showText(self):    
        
        text = Label(self, text = "Hey There")
        text.pack()
    
        
root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop()