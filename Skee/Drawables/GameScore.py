import pygame
from Elements.RectEntity import *
from Elements.TextEntity import *
from Drawables.Drawable import *

WHITE = (255,251,252)
GREY = (48,51,46)
PINK = (236,5,142)
BLACK = (1,4,0)
BLUE = (98,187,193)

class GameScore(Drawable):
    Frame = 0
    IsActive = True

    def __init__(self, screen):
        self.Screen = screen
        self.LeftBackground = RectEntity(screen, 0,0,635,1080,WHITE)
        self.RightBackground = RectEntity(screen, 635,0,1285,1080,GREY)
        self.Name = TextEntity(screen, "", 100, 0 ,70 ,PINK, 635, GREY, 4)
        self.RemainingNumber = TextEntity(screen, "", 650, 0, 130, BLACK, 635, GREY, 10)
        self.Balls = TextEntity(screen, "Balls", 140, 0, 805, GREY, 635, BLACK,5)
        self.ScoreText = TextEntity(screen, "Score:", 140, 635, 50, BLUE,1920,BLACK,5)
        self.ScoreValue = TextEntity(screen, "", 700, 635, 70, PINK,1920,WHITE,5)

    def Draw(self, gameState):
        self.LeftBackground.Draw()
        self.RightBackground.Draw()
        
        self.Name.Text = gameState.PlayerName.upper()
        self.Name.Draw()
        
        self.RemainingNumber.Text = str(gameState.Balls)
        self.RemainingNumber.Draw()

        self.Balls.Draw()
        self.ScoreText.Draw()

        self.ScoreValue.Text = (format (gameState.Score, ',d'))
        self.ScoreValue.Draw()