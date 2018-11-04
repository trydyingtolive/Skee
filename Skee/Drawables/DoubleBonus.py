import pygame
import time
from Elements.RectEntity import *
from Elements.TextEntity import *
from Drawables.Drawable import *
from Utilities.GameColors import *

class DoubleBonus(Drawable):
    def __init__(self, gameState):
        self.StartTime = time.time()*1000
        self.GameState = gameState
        self.Background = RectEntity(gameState.Screen,0,0,1920,1080,PINK)
        self.DoubleText = TextEntity(gameState.Screen, "Double", 460, 0 ,34 ,WHITE, 1167, BLUE, 15)
        self.BonusText = TextEntity(gameState.Screen, "Bonus", 460, 0 , 460, WHITE, 1167, BLUE, 15)
        self.SevenText = TextEntity(gameState.Screen, "+7", 973, 1079 , -58, BLUE, 1920, BLACK, 20)

    def Draw(self):
        self.Background.Draw()
        self.DoubleText.Draw()
        self.BonusText.Draw()
        self.SevenText.Draw()

    def IsActive(self):
        if ((time.time()*1000) - 3000) > self.StartTime:
            return False
        return True