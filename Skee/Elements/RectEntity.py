import pygame

class RectEntity(object):

    def __init__(self, screen, x=0, y=0,w=0,h=0, color=(255,255,255)):
        self.Screen = screen
        self.X = x
        self.Y = y
        self.W = w
        self.H = h
        self.Color = color
        

    def Draw(self):
        pygame.draw.rect(self.Screen, self.Color, (self.X, self.Y, self.W,self.H))
