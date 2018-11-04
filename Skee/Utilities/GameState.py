from Drawables.DoubleBonus import *
from Drawables.Bonus import *
from Drawables.FinalScore import *

class GameState(object):
    PlayerId = 0
    PlayerName = "Chuck"
    Score = 0
    Balls = 9
    Bonus = False
    DoubleBonus = False
    Drawables = []
    Screen = None

    def __init__(self, screen):
        self.Screen = screen


    def AddScore(self, points):
        prevScore = self.Score
        self.Score += points
        self.Balls += -1
        if prevScore < 200 and self.Score >= 200 :
            self.Bonus = True
            self.Balls += 8
            self.Drawables.append(Bonus(self))
        if prevScore < 410 and self.Score >= 410:
            self.DoubleBonus = True
            self.Balls += 7
            self.Drawables.append(DoubleBonus(self))
        if self.Balls == 0:
            self.Drawables.append(FinalScore(self))
