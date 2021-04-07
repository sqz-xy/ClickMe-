#By sq-zxy
#07/04/2021

#TODO:
# Timer

#ttkthemes imports
from tkinter import ttk

#Tkinter Imports
import tkinter as tk
from tkinter import *

#Random library
import random

#Time library
import time

#Global variables
elapsedTime = 0.0
startTime = None

#Main App Class
class ClickMe(tk.Tk):
    #Constructor for the class
    def __init__(self):
        super().__init__()

        #Instance Variables
        self._randX = 0
        self._randY = 0
        self._clickCounterInt = 0
        self._averageSecs = 0.0

        #Global variable use
        global elapsedTime

        #Window Geometry
        self.title('ClickMe!')
        self.geometry('400x300')
        self.resizable(0, 0)
        self.style = ttk.Style().theme_use('vista')

        #Greeting Label
        self.greeting = ttk.Label(self, text="Welcome to ClickMe! The goal is...")
        self.greeting.pack()

        #Click Counter
        self.clickCounter = ttk.Label(self, text = str(0))
        self.clickCounter.place(x = 325, y = 236)
        self.clickCounter.config(font = ("Impact", 35))

        #Text label for Click Counter
        self.clickCounterInfo = ttk.Label(self, text = "Total Clicks:")
        self.clickCounterInfo.place(x = 300, y = 225)
        self.clickCounterInfo.config(font = ("Impact", 11))

        #Average time between clicks 
        self.timerValue = ttk.Label(self, text = str(0.0))
        self.timerValue.place(x = 50, y = 236)
        self.timerValue.config(font = ("Impact", 35))

        #Text label for timerValue
        self.timerValueInfo = ttk.Label(self, text = "Average time between clicks:")
        self.timerValueInfo.place(x = 0, y = 225)
        self.timerValueInfo.config(font = ("Impact", 11))

        #ClickMeButton
        self.clickMeButton = ttk.Button(text = "Click me!", command = self.OnClick)
        self.clickMeButton.place(x = 160, y = 140)

    #Calculates the average amount of clicks
    def calculateClickAverage(self):
        elapsedTime = time.time() - startTime
        _averageSecs = float(elapsedTime) / float(self._clickCounterInt)
        _averageSecs = round(_averageSecs, 2)
        self.timerValue.config(text = str(_averageSecs))

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

        #Calculates the average amount of time between clicks
        self.calculateClickAverage()

        #Moves the button to a random place on the screen
        self.genRandomX(), self.genRandomY()
        self.clickMeButton.place(x = self._randX, y = self._randY)

#Runs the program
if __name__ == "__main__":
    startTime = time.time()
    ClickMeApp = ClickMe()
    ClickMeApp.mainloop()
