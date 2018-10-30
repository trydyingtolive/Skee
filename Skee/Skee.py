#import RPi.GPIO as GPIO
import time
import pygame
from Eventhandlers.KeyPress import *
from Utilities.GameState import *
from Drawables.GameScore import *

##This boolean kills our loop if false
running = True
keyboardEvents = []

def setup():
    # Set up GPIO
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Skee")
    global screen
    screen = pygame.display.set_mode((1920,1080))
    global gameState
    gameState = GameState(screen)
    ##pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    global gameScore
    gameScore = GameScore(screen)
    gameState.Drawables.append(gameScore)
    
    keyboardEvents.append(KeyPress(pygame.K_1, addTen))
    keyboardEvents.append(KeyPress(pygame.K_2, addTwenty))
    keyboardEvents.append(KeyPress(pygame.K_3, addThirty))
    keyboardEvents.append(KeyPress(pygame.K_4, addForty))
    keyboardEvents.append(KeyPress(pygame.K_5, addFifty))


def loop():
    global running
    global gameState
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    running = False
                HandleKeyEvent(event.key)
    UpdateDisplay()

def addTen():
    global gameState
    gameState.AddScore(10)

def addTwenty():
    global gameState
    gameState.AddScore(20)

def addThirty():
    global gameState
    gameState.AddScore(30)

def addForty():
    global gameState
    gameState.AddScore(40)

def addFifty():
    global gameState
    gameState.AddScore(50)

def HandleKeyEvent(key):
    for eventHandler in keyboardEvents:
        if eventHandler.Key == key:
            eventHandler.Callback()

def UpdateDisplay():
     screen.fill((48,51,46))

     for drawable in gameState.Drawables:
         drawable.Frame +=1

     while(True):
         if (gameState.Drawables[-1].IsActive):
             gameState.Drawables[-1].Draw(gameState)
             break
         else: 
            gameState.Drawables.pop()
     pygame.display.flip()

if __name__ == "__main__":
    setup()
    while running:
        loop()