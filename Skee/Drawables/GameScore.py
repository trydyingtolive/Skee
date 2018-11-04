from Elements.RectEntity import *
from Elements.TextEntity import *
from Drawables.Drawable import *
from Utilities.GameColors import *


class GameScore(Drawable):

    def __init__(self, gameState):
        self.GameState = gameState
        self.LeftBackground = RectEntity(gameState.Screen, 0,0,635,1080,WHITE)
        self.RightBackground = RectEntity(gameState.Screen, 635,0,1285,1080,GREY)
        self.Name = TextEntity(gameState.Screen, "", 100, 0 ,70 ,PINK, 635, GREY, 4)
        self.RemainingNumber = TextEntity(gameState.Screen, "", 650, 0, 130, BLACK, 635, GREY, 10)
        self.Balls = TextEntity(gameState.Screen, "Balls", 140, 0, 805, GREY, 635, BLACK,5)
        self.ScoreText = TextEntity(gameState.Screen, "Score:", 140, 635, 50, BLUE,1920,BLACK,5)
        self.ScoreValue = TextEntity(gameState.Screen, "", 700, 635, 70, PINK,1920,WHITE,5)

    def Draw(self):
        self.LeftBackground.Draw()
        self.RightBackground.Draw()
        
        self.Name.Text = self.GameState.PlayerName.upper()
        self.Name.Draw()
        
        self.RemainingNumber.Text = str(self.GameState.Balls)
        self.RemainingNumber.Draw()

        self.Balls.Draw()
        self.ScoreText.Draw()

        self.ScoreValue.Text = (format (self.GameState.Score, ',d'))
        self.ScoreValue.Draw()

    def IsActive(self):
        return self.GameState.Balls > 0