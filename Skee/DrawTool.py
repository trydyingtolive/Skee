#import RPi.GPIO as GPIO
import time
import pygame
from Eventhandlers.KeyPress import *
from Elements.RectEntity import *
from Elements.TextEntity import *


##This boolean kills our loop if false
textItems = ["1,200", "Personal Best", "High Score"]
x = 0
y = 0
w = 1920
pt = 24
running = True
keyboardEvents = []
keyMethod = None
textEntities = []
current = 0
dataEntity = None

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
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    global textItems
    global textEntities
    for item in textItems:
        textEntities.append(TextEntity(screen, item))
    global dataEntity
    dataEntity = TextEntity(screen, "")
    
    keyboardEvents.append(KeyPress(pygame.K_UP, up))
    keyboardEvents.append(KeyPress(pygame.K_DOWN, down))
    keyboardEvents.append(KeyPress(pygame.K_LEFT, left))
    keyboardEvents.append(KeyPress(pygame.K_RIGHT, right))
    keyboardEvents.append(KeyPress(pygame.K_z, unbiggen))
    keyboardEvents.append(KeyPress(pygame.K_x, embiggen))
    keyboardEvents.append(KeyPress(pygame.K_TAB, next))
    keyboardEvents.append(KeyPress(pygame.K_COMMA, narrow))
    keyboardEvents.append(KeyPress(pygame.K_PERIOD, widen))


def loop():
    global running
    global keyMethod

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                else:
                    HandleKeyEvent(event.key)
            elif event.type == pygame.KEYUP:
                keyMethod = None
    if keyMethod:
        keyMethod()
    UpdateDisplay()

def up():
    global y
    y = y - 1
    UpdateDisplay()

def down():
    global y
    y = y + 1
    UpdateDisplay()

def left():
    global x
    x = x - 1
    UpdateDisplay()

def right():
    global x
    x = x + 1
    UpdateDisplay()

def unbiggen():
    global pt
    pt = pt - 1
    UpdateDisplay()

def embiggen():
    global pt
    pt = pt + 1
    UpdateDisplay()

def narrow():
    global w
    w = w - 1
    UpdateDisplay()

def widen():
    global w
    w = w + 1
    UpdateDisplay()

def next():
    global current
    if current + 1 >= len(textEntities):
        current = 0
    else:
        current +=1
    entity = textEntities[current]
    global x
    global y
    global pt
    global w
    x = entity.X
    y = entity.Y
    pt = entity.FontSize
    w = entity.End
    UpdateDisplay()


def HandleKeyEvent(key):
    for eventHandler in keyboardEvents:
        if eventHandler.Key == key:
            global keyMethod
            keyMethod = eventHandler.Callback

def UpdateDisplay():
     screen.fill((0,0,0))
     global textEntities
     global current
     global dataEntity
     global x
     global y
     global pt
     global w

     for i in range(len( textEntities)):
         if i == current:
             textEntities[i].X=x
             textEntities[i].Y=y
             textEntities[i].FontSize = pt
             textEntities[i].End = w
             textEntities[i].Color = (255,255,255)
         else:
             textEntities[i].Color = (100,100,100)
         textEntities[i].Draw()
     dataEntity.Text = "PT:{2} X:{0} Y:{1} W: {3}".format(x, y, pt, w)
     dataEntity.Draw()
     pygame.display.flip()

if __name__ == "__main__":
    setup()
    while running:
        loop()