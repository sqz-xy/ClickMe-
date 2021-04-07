#By sq-zxy
#07/04/2021

#Imports 
from tkinter import *
import tkinter as tk

#Declaring the top level widget
window = tk.Tk()
window.title('ClickMe!')
window.geometry('400x300')
window.resizable(0, 0)

greeting = tk.Label(text="Welcome to ClickMe!\nThe goal is... to click me")
greeting.pack()



#def OnClick:


clickCounter = tk.Label(text = str(0))
clickCounter.place(relx = 1.0, rely = 1.0, anchor = SE)

clickMeButton = tk.Button(text = "Click me!", width = 10, height = 2)
clickMeButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#Calling the program
window.mainloop()
