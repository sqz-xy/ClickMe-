#By sq-zxy
#07/04/2021

#Imports 
from tkinter import *
import tkinter as tk

#Declaring the top level widget
window = tk.Tk()
window.title('ClickMe!')
window.geometry('300x200')
window.resizable(0, 0)

greeting = tk.Label(text="Welcome to ClickMe!\nThe goal is... to click me")
greeting.pack()

ClickMeButton = tk.Button(text = "Click me!", width = 25, height = 5)
ClickMeButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#Calling the program
window.mainloop()
