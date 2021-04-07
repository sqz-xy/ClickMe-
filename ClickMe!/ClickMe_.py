#By sq-zxy
#07/04/2021

#Imports 
from tkinter import *
import tkinter as tk
import random

#Declaring the top level widget
window = tk.Tk()
window.title('ClickMe!')
window.geometry('400x300') # x = 400, y = 300
window.resizable(0, 0)

#Variabless
clickCounterInt = 0
randX = 0
randY = 0

greeting = tk.Label(text="Welcome to ClickMe!\nThe goal is... to click me")
greeting.pack()

#Generates a random X coordinate
def genRandomX():
    global randX
    randX = random.randint(0, 375)

#Generates a random Y coordinate
def genRandomY():
    global randY
    randY = random.randint(0, 275)

#Button click action
def OnClick():
    global clickCounterInt
    clickCounterInt += 1
    clickCounter.config(text = str(clickCounterInt))

    genRandomX(), genRandomY()
    clickMeButton.place(x = randX, y = randY)


clickCounter = tk.Label(text = str(0))
clickCounter.place(relx = 1.0, rely = 1.0, anchor = SE)
clickCounter.config(font = ("Impact", 35))

clickMeButton = tk.Button(text = "Click me!", width = 10, height = 2, command = OnClick)
clickMeButton.place(x = 160, y = 140)

#Calling the program
window.mainloop()
