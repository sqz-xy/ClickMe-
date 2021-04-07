#By sq-zxy
#07/04/2021

#TODO:
# Fix the Image imports

#ttkthemes imports
from tkinter import ttk

#Tkinter Imports
import tkinter as tk
from tkinter import *

#Pillow Imports
from PIL import ImageTk, Image

#Random library
import random

#Time library
import time

#Pygame
import pygame

#Global variables
elapsedTime = 0.0
startTime = None

#Main App Class
class ClickMe(tk.Tk):
    #Constructor for the class
    def __init__(self):
        super().__init__()

        #Random vars
        self._randX = 0
        self._randY = 0
        self._randSong = 0

        #Counter vars
        self._clickCounterInt = 0
        self._averageSecs = 0.0

        #Initializes the mixer and the sounds
        pygame.mixer.init()
        self._sound1 = pygame.mixer.Sound("oggy.mp3")
        self._sound1.set_volume(0.03)
        self._sound2 = pygame.mixer.Sound("yuh.mp3")
        self._sound2.set_volume(0.03)
        self._sound3 = pygame.mixer.Sound("thud.mp3")
        self._sound3.set_volume(0.03)
        self._sound4 = pygame.mixer.Sound("givehimtome.mp3")
        self._sound4.set_volume(0.11)

        #Array of sounds
        self._sounds = [self._sound2, self._sound3, self._sound4]

        #Target image path and default size
        self._buttonSizeX = 100
        self._buttonSizeY = 100
        self._targetPath = "target.png"

        #Target image
        self._target = Image.open(self._targetPath)
        self._target = self._target.resize((self._buttonSizeX, self._buttonSizeY), Image.ANTIALIAS)
        self._target = ImageTk.PhotoImage(self._target)

        #Global variable use
        global elapsedTime

        #Window Geometry
        self.title('ClickMe!')
        self.geometry('400x300')
        self.resizable(0, 0)
        self.iconbitmap("DEhzsgnXcAMatG0.ico")
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
        self.clickMeButton = tk.Button(text = "Click me!", image = self._target, width = self._buttonSizeX, height = self._buttonSizeY, command = self.OnClick)
        self.clickMeButton.place(x = 145, y = 100)

    #Plays one of the sound effects
    def playSound(self):
        self._randSong = random.randint(0, len(self._sounds))
        self._sounds[self._randSong - 1].play()

    #Resizes the button on click
    def resizeButton(self):
        if(self._buttonSizeX <= 5 & self._buttonSizeY <= 5):
            return
        else:
            self._buttonSizeX -= 1
            self._buttonSizeY -= 1

        self._target = Image.open(self._targetPath)
        self._target = self._target.resize((self._buttonSizeX, self._buttonSizeY), Image.ANTIALIAS)
        self._target = ImageTk.PhotoImage(self._target)
        self.clickMeButton.config(width = self._buttonSizeX, height = self._buttonSizeY, image = self._target)

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
        #Plays the sound on press
        self.playSound()

        #Increments the click counter
        self._clickCounterInt += 1
        self.clickCounter.config(text = str(self._clickCounterInt))

        #Celebration sound every 10 clicks
        if(self._clickCounterInt % 15 == 0):
            self._sound1.play()

        #Calculates the average amount of time between clicks
        self.calculateClickAverage()

        #Moves the button to a random place on the screen
        self.genRandomX(), self.genRandomY()
        self.clickMeButton.place(x = self._randX, y = self._randY)

        #Resizes the button
        self.resizeButton()

#Runs the program
if __name__ == "__main__":
    startTime = time.time()
    ClickMeApp = ClickMe()
    ClickMeApp.mainloop()
