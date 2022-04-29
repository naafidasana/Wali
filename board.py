import pygame as pg
from pygame.sprite import Sprite
import pygame.font


class Board(Sprite):

    "Wali (Oware) Board"
    def __init__(self, screen):
        # Wali board contains 12 holes, 6 per each player's side,
        # and 4 marbles in each holes at the default state.
        self.board = [4] * 12

        self.p1_wins = 0
        self.p2_wins = 0

        self.screen = screen

        # Font settings
        self.font = pygame.font.SysFont(None, 36)
        self.font_color = (245,245,245)

        # Load Images to represent empty, default and different board states.
        self.board_image = pg.image.load('images/board01.jpg')
        self.board_rect = self.board_image.get_rect()

        self.board_rect.x = 0
        self.board_rect.y = 0
        self.draw()

    def draw(self):
        """ Draw an oware board with the appropriate number of marbles
        in each hole onto the screen."""
        # Draw board on the screen
        self.screen.blit(self.board_image, self.board_rect)

        # Mark each hole in side 1 with the appropriate number, ranging from 1 - 6
        # starting from the left
        num_image_rect = [160, 530]
        for i in range(1, 7):
            num_image = self.font.render(str(i), True, self.font_color)
            self.screen.blit(num_image, num_image_rect)
            num_image_rect[0] += 180

        # Mark each hole in side 2 with the appropriate number, ranging from 1 to 6
        # starting from the right
        num_image_rect = [160, 106]
        for i in range(-6, 0):
            num_image = self.font.render(str(-i), True, self.font_color)
            self.screen.blit(num_image, num_image_rect)
            num_image_rect[0] += 180

    def update(self):
        """Load the appropriate image if the state of the board changes."""

        # Upload images that represent holes with 1-15 marbles into a python dictionary
        self.h_imgs = {
        0: pg.transform.scale(pg.image.load('images/00.png'), [160, 160]), 1: pg.transform.scale(pg.image.load('images/01.png'),[160, 160]),
        2: pg.transform.scale(pg.image.load('images/02.png'), [160, 160]), 3: pg.transform.scale(pg.image.load('images/03.png'),[160, 160]),
        4: pg.transform.scale(pg.image.load('images/04.png'), [160, 160]), 5: pg.transform.scale(pg.image.load('images/05.png'),[160, 160]),
        6: pg.transform.scale(pg.image.load('images/06.png'), [160, 160]), 7: pg.transform.scale(pg.image.load('images/07.png'),[160, 160]),
        8: pg.transform.scale(pg.image.load('images/08.png'),[160, 160]), 9: pg.transform.scale(pg.image.load('images/09.png'),[160, 160]),
        10: pg.transform.scale(pg.image.load('images/10.png'),[160, 160]), 11: pg.transform.scale(pg.image.load('images/11.png'),[160, 160]),
        12: pg.transform.scale(pg.image.load('images/12.png'),[160, 160]), 13: pg.transform.scale(pg.image.load('images/13.png'),[160, 160]),
        14: pg.transform.scale(pg.image.load('images/14.png'), [160, 160]), 15: pg.transform.scale(pg.image.load('images/15.png'),[160, 160])}

        starting_rect = [87, 330]

        # Check the current board state and draw the appropriate image
        # to represent the number of marbles in each hole in first side of board
        for i in range(0,6):
            if self.board[i] >= 15:
                self.screen.blit(self.h_imgs[15], starting_rect)
            elif self.board[i] == 0:
                self.screen.blit(self.h_imgs[0], starting_rect)
            elif self.board[i] == 1:
                self.screen.blit(self.h_imgs[1], starting_rect)
            elif self.board[i] == 2:
                self.screen.blit(self.h_imgs[2], starting_rect)
            elif self.board[i] == 3:
                self.screen.blit(self.h_imgs[3], starting_rect)
            elif self.board[i] == 4:
                self.screen.blit(self.h_imgs[4], starting_rect)
            elif self.board[i] == 5:
                self.screen.blit(self.h_imgs[5], starting_rect)
            elif self.board[i] == 6:
                self.screen.blit(self.h_imgs[6], starting_rect)
            elif self.board[i] == 7:
                self.screen.blit(self.h_imgs[7], starting_rect)
            elif self.board[i] == 8:
                self.screen.blit(self.h_imgs[8], starting_rect)
            elif self.board[i] == 9:
                self.screen.blit(self.h_imgs[9], starting_rect)
            elif self.board[i] == 10:
                self.screen.blit(self.h_imgs[10], starting_rect)
            elif self.board[i] == 11:
                self.screen.blit(self.h_imgs[11], starting_rect)
            elif self.board[i] == 12:
                self.screen.blit(self.h_imgs[12], starting_rect)
            elif self.board[i] == 13:
                self.screen.blit(self.h_imgs[13], starting_rect)
            elif self.board[i] == 14:
                self.screen.blit(self.h_imgs[14], starting_rect)
            starting_rect[0] += 180

        # Check the current board state and draw the appropriate image
        # to represent the number of marbles in each hole in second side of board
        starting_rect = [87, 150]
        for i in range(-1,-7,-1):
            if self.board[i] >= 15:
                self.screen.blit(self.h_imgs[15], starting_rect)
            elif self.board[i] == 0:
                self.screen.blit(self.h_imgs[0], starting_rect)
            elif self.board[i] == 1:
                self.screen.blit(self.h_imgs[1], starting_rect)
            elif self.board[i] == 2:
                self.screen.blit(self.h_imgs[2], starting_rect)
            elif self.board[i] == 3:
                self.screen.blit(self.h_imgs[3], starting_rect)
            elif self.board[i] == 4:
                self.screen.blit(self.h_imgs[4], starting_rect)
            elif self.board[i] == 5:
                self.screen.blit(self.h_imgs[5], starting_rect)
            elif self.board[i] == 6:
                self.screen.blit(self.h_imgs[6], starting_rect)
            elif self.board[i] == 7:
                self.screen.blit(self.h_imgs[7], starting_rect)
            elif self.board[i] == 8:
                self.screen.blit(self.h_imgs[8], starting_rect)
            elif self.board[i] == 9:
                self.screen.blit(self.h_imgs[9], starting_rect)
            elif self.board[i] == 10:
                self.screen.blit(self.h_imgs[10], starting_rect)
            elif self.board[i] == 11:
                self.screen.blit(self.h_imgs[11], starting_rect)
            elif self.board[i] == 12:
                self.screen.blit(self.h_imgs[12], starting_rect)
            elif self.board[i] == 13:
                self.screen.blit(self.h_imgs[13], starting_rect)
            elif self.board[i] == 14:
                self.screen.blit(self.h_imgs[14], starting_rect)
            starting_rect[0] += 180
