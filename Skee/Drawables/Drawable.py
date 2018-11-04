import time

class Drawable(object):
    StartTime = time.time() *1000
    GameState = None

    def _init_(self, gameState):
        self.GameState = gameState

    def IsActive(self):
        return True

    def Draw(self):
        pass