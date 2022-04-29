import pygame
from pygame.constants import K_1, K_2, K_3, K_4, K_5, K_6
import sys


def check_events():
    '''Check for events from the user.'''
    for event in pygame.event.get():
        # Quit game if user clicks the close button.
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()

        # Handle mouse cicks.
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == K_1:
                return 1
            if event.key == K_2:
                return 2
            if event.key == K_3:
                return 3
            if event.key == K_4:
                return 4
            if event.key == K_5:
                return 5
            if event.key == K_6:
                return 6
            

def get_move(player, pick_from, board):
    '''Use the pick_from value provided by the user to initiate player movement.'''
    player.move(pick_from, board)

def update_screen(board, stats):
    '''Update the pygame screen in accordance with the current
    state of the board and game settings.'''

    # Draw and update board on screen if game is active.
    # By default, game_active = False
    if not stats.game_active:
        board.draw
    
    board.update()

    ##   play_button.draw()


def can_proceed(board, stats, turn, font, screen, gs):
    '''Determine if game can proceed.
    When there are less than 6 marbles left, game can drag on for a long time.
    We will thus end the game and add the marbles in each player's side to his
    wins.'''
    if sum(board.board) < 6:
        stats.game_active = False

    # When it's a particular player's turn and he/she
    # has no marbles to move with, end game.
    if turn == 1 and sum(board.board[0:6:1]) == 0:
        stats.game_active = False
        # Add marbles in player's side to his wins.
        for ndx in range(6):
            board.p1_wins += board.board[ndx]
            board.board[ndx] = 0

            # Notify players of current state.
            alert = font.render("Player One has No Marbles To Move!!! Game Ended", True, [255,255,255], gs.bg_color)
            screen.blit(alert, [300, 20])

    elif turn == 2 and sum(board.board[6:12:1]) == 0:
        stats.game_active = False
        # Add marbles in player's side to his wins.
        for ndx in range(board.board[6:12:1]):
            board.p2_wins += board.board[ndx]
            board.board[ndx] = 0

            # Notify players of current state.
            alert = font.render("Player One has No Marbles To Move!!! Game Ended", True, [255,255,255], gs.bg_color)
            screen.blit(alert, [300, 20])
