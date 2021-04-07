#By sq-zxy
#07/04/2021

#Imports 
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random

class ClickMe(tk.Tk):

    #Constructor for the class
    def __init__(self):
        super().__init__()

        #Instance Variables
        self._randX = 0
        self._randY = 0
        self._clickCounterInt = 0

        #Window Geometry
        self.title('ClickMe!')
        self.geometry('400x300')
        self.resizable(0, 0)

        #Greeting Label
        self.greeting = tk.Label(self, text="Welcome to ClickMe!\nThe goal is... to click me")
        self.greeting.pack()

        #Click Counter
        self.clickCounter = tk.Label(self, text = str(0))
        self.clickCounter.place(relx = 1.0, rely = 1.0, anchor = SE)
        self.clickCounter.config(font = ("Impact", 35))

        #ClickMeButton
        self.clickMeButton = tk.Button(text = "Click me!", width = 10, height = 2, command = self.OnClick)
        self.clickMeButton.place(x = 160, y = 140)

    #Generates a random X coordinate
    def genRandomX(self):
        self._randX = random.randint(0, 375)

    #Generates a random Y coordinate
    def genRandomY(self):
        self._randY = random.randint(0, 275)

    #Button click action
    def OnClick(self):
        #Increments the click counter
        self._clickCounterInt += 1
        self.clickCounter.config(text = str(self._clickCounterInt))

        #Moves the button to a random place on the screen
        self.genRandomX(), self.genRandomY()
        self.clickMeButton.place(x = self._randX, y = self._randY)

#Runs the program
if __name__ == "__main__":
    ClickMeApp = ClickMe()
    ClickMeApp.mainloop()
