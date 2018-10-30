import pygame
from Elements.RectEntity import *
from Elements.TextEntity import *
from Drawables.Drawable import *

WHITE = (255,251,252)
GREY = (48,51,46)
PINK = (236,5,142)
BLACK = (1,4,0)
BLUE = (98,187,193)

class Animation(Drawable):
    def __init__(self, screen):
        self.Screen = screen;
        self.Text = TextEntity(screen, "TEST", 100, 0 ,70 ,PINK, 635, GREY, 4)
        self.Text2 = TextEntity(screen, "TEST", 100, 0 ,70 ,GREY, 635, PINK, 4)

    def Draw(self, gameState):
        self.Text.Text = str(self.Frame)
        self.Text.Draw()
        if self.Frame > 300:
            self.IsActive = False
