import pygame
import time
from Elements.RectEntity import *
from Elements.TextEntity import *
from Drawables.Drawable import *
from Utilities.GameColors import *

class FinalScore(Drawable):
    def __init__(self, gameState):
        self.StartTime = time.time()*1000
        self.GameState = gameState
        self.Background = RectEntity(gameState.Screen,0,0,1920,1080,BLACK)
        self.ScoreText = TextEntity(gameState.Screen, "", 581, 0 ,181, WHITE)
        self.TopText = TextEntity(gameState.Screen, "High Score", 217, 0 , 5, WHITE, 1920)
        self.BottomText = TextEntity(gameState.Screen, "Personal Best", 217, 0 , 806, WHITE)

    def Draw(self):
        self.Background.Draw()
        self.ScoreText.Text = (format (self.GameState.Score, ',d'))

        self.ScoreText.Draw()
        self.TopText.Draw()
        self.BottomText.Draw()

    def IsActive(self):
        if ((time.time()*1000) - 6000) > self.StartTime:
            return False
        return True