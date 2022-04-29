import pygame
from pygame.sprite import Sprite

class Settings:

    '''Class to keep track of game settings.'''
    def __init__(self):
        # Initialize static settings.
        self.swidth = 1200
        self.sheight = 676
        self.bg_color = [47,65,58]


class Stats:

    '''Class to keep track of game statistics.'''
    def __init__(self):
        self.game_active = False


class Button(Sprite):

    '''Class to represent buttons.'''
    def __init__(self,msg, font, screen, gs):
        self.width = 200
        self.height = 90
        self.msg = msg
        self.font = font
        self.screen = screen
        self.gs = gs

        # Create rect attribute
        self.rect = pygame.Rect((600,50), (100,400))

    def draw(self):
        msg = self.font.render(self.msg, True, [215,194,194], self.gs.bg_color)
        self.screen.blit(msg, self.rect)
