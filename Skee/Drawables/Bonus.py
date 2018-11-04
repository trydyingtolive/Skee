import pygame
import time
from Elements.RectEntity import *
from Elements.TextEntity import *
from Drawables.Drawable import *
from Utilities.GameColors import *

class Bonus(Drawable):
    def __init__(self, gameState):
        self.StartTime = time.time()*1000
        self.GameState = gameState
        self.Background = RectEntity(gameState.Screen,0,0,1920,1080,BLUE)
        self.BonusText = TextEntity(gameState.Screen, "Bonus!", 767, 0 ,7 ,PINK, 1920, BLACK, 15)
        self.BallsText = TextEntity(gameState.Screen, "+8 Balls", 205, 0 , 810, GREY, 1920, WHITE, 6)

    def Draw(self):
        self.Background.Draw()
        self.BonusText.Draw()
        if ((time.time()*1000) - 1500) > self.StartTime:
            self.BallsText.Draw()

    def IsActive(self):
        if ((time.time()*1000) - 3000) > self.StartTime:
            return False
        return True