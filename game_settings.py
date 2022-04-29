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


class Button:

    '''Class to represent buttons.'''
    def __init__(self):
        self.width = 200
        self.height = 90

    def draw(self):
        pass
