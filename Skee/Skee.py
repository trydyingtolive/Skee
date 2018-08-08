#import RPi.GPIO as GPIO
import time
import pygame
from Eventhandlers.KeyPress import *
from Drawables.TextEntity import *

##This boolean kills our loop if false
running = True
drawables = []
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
    screen = pygame.display.set_mode((1920,1080))
    ##pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((48,51,46))
    entity = TextEntity(screen, "A Line", 300,0,0,(255,0,255),shadow = (255,255,255), shadowOffset=9)
    entity.Draw()
    pygame.display.flip()
    keyboardEvents.append(KeyPress(pygame.K_1, addTen))
    keyboardEvents.append(KeyPress(pygame.K_2, addTwenty))
    keyboardEvents.append(KeyPress(pygame.K_3, addThirty))
    keyboardEvents.append(KeyPress(pygame.K_4, addForty))
    keyboardEvents.append(KeyPress(pygame.K_5, addFifty))

def addTen():
    print("10")

def addTwenty():
    print("20")

def addThirty():
    print("30")

def addForty():
    print("40")

def addFifty():
    print("50")

def HandleKeyEvent(key):
    for eventHandler in keyboardEvents:
        if eventHandler.Key == key:
            eventHandler.Callback()

if __name__ == "__main__":
    setup()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    running = False
                HandleKeyEvent(event.key)