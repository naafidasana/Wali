import pygame
from pygame.sprite import Sprite
from time import sleep

class Player(Sprite):

    "Class to Represent players of the wali (oware) game."
    def __init__(self, num, name = None):
        # Initialize player identifiers
        self.num = num
        self.name = name

        # While player is moving, use the potentialWins variable to keep track of
        # the holes player adds to in the opponent's side.
        # This will be used to determine if player's move resulted in a gain or not.
        self.potentialWins = []
        

    def move(self, pick_from, board):
        '''Handle movement of player.
        Player picks marbles from a non-empty hole on his side and
        adds one marble to all subsequent holes till the marbles he picked
        finishes.'''
        

        # Handle movement for player 1.
        if self.num == 1:
            marbles_picked = board.board[pick_from - 1]  # self.board_state[0:6] -> Player One.
            board.board[pick_from - 1] = 0      # Empty the hole picked from
            add_to = pick_from     # Next hole from where player picked from.
            while marbles_picked > 0:
                if add_to == 12:    # End of board, loop back around to the beginning.
                    add_to = 0

                # Check if player 1 is adding to the opponent's side.
                if 6 <= add_to <= 11:
                    self.potentialWins.append(add_to)
                else:
                    self.potentialWins = []
                board.board[add_to] += 1
                board.update()
                pygame.display.update()
                sleep(0.27)
                marbles_picked -= 1
                add_to += 1

            self.handleWin(self.potentialWins, board)

        # Handle movement for player 2.
        elif self.num == 2:
            marbles_picked = board.board[pick_from + 5]    # self.board_state[6:12] -> Player Two
            board.board[pick_from + 5] = 0      # Empty the hole picked from
            add_to = pick_from + 6      # Next hole from where player picked from.
            while marbles_picked > 0:
                if add_to == 12:    # End of board, loop back around to the beginning.
                    add_to = 0

                # Check if player 2 is adding to the opponent's side.
                if 0 <= add_to <= 5:
                    self.potentialWins.append(add_to)
                else:
                    self.potentialWins = []
                board.board[add_to] += 1
                board.update()
                pygame.display.update()
                sleep(0.27)
                marbles_picked -= 1
                add_to += 1
        
            self.handleWin(self.potentialWins, board)

    def handleWin(self, potentialWins, board):
        '''Keep track of player's movement to determine if move resulted in scoring
        or not. Player can only score when he ends on the opponent's side and
        brings the total marble count in the hole(or consecutive holes) he
        ended on to 2 or 3. If player scored, add marbles scored to his wins.'''

        if len(potentialWins) < 1:
            return

        # Handle wins for player 1.
        if self.num == 1:
            for ndx in potentialWins[::-1]:
                if 2 <= board.board[ndx] <= 3:
                    marbles_won = board.board[ndx]
                    board.p1_wins += marbles_won
                    board.board[ndx] = 0
                    pygame.display.update()
                    sleep(0.27)
                else:
                    break

            # If player 1's move resulted in scoring from all holes in the
            # opponent's side, leave the marbles in the first hole to the opponent.
            if len(self.potentialWins) > 1 and sum(board.board[6:12:1]) == 0:
                board.board[6] = marbles_won
                board.p1_wins -= marbles_won
                pygame.display.update()
                sleep(0.27)

        # Handle wins for player 2.
        elif self.num == 2:
            for ndx in potentialWins[::-1]:
                if 2 <= board.board[ndx] <= 3:
                    marbles_won = board.board[ndx]
                    board.p2_wins += marbles_won
                    board.board[ndx] = 0
                    pygame.display.update()
                    sleep(0.27)
                else:
                    break
            
            # If player 2's move resulted in scoring from all holes in the
            # opponent's side, leave the marbles in the first hole to the opponent.
            if len(self.potentialWins) > 1 and sum(board.board[0:6:1]) == 0:
                board.board[0] = marbles_won
                board.p2_wins -= marbles_won
                pygame.display.update()
                sleep(0.27)
