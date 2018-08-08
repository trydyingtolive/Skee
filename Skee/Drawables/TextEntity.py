import pygame

class TextEntity(object):

    def __init__(self, screen, text="", fontsize=24, x=0, y=0, color=(255,255,255), end=1920, shadow=None, shadowOffset=4):
        self.Screen = screen
        self.Text = text
        self.FontSize = fontsize
        self.X = x
        self.Y = y
        self.Color = color
        self.End = end
        self.Shadow = shadow
        self.ShadowOffset = shadowOffset

    def Draw(self):
        myfont = pygame.font.SysFont("Skee", self.FontSize)
        label = myfont.render(self.Text, 1, self.Color)
        w = label.get_rect().width
        x = ((self.End - self.X)/2)-(w/2)
        if self.Shadow:
            shadow = myfont.render(self.Text, 1, self.Shadow)
            self.Screen.blit(shadow, (x+self.ShadowOffset, self.Y+self.ShadowOffset))
        self.Screen.blit(label, (x, self.Y))