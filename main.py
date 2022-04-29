import pygame
from board import Board
from player import Player
from game_settings import Settings, Stats, Button
import game_functions as gf


def main():
    # Main game loop.
    # Initialize pygame.
    pygame.init()

    gs = Settings()     # gs represents game settings
    stats = Stats()     # keep track of game statistics

    screen = pygame.display.set_mode((gs.swidth, gs.sheight))
    pygame.display.set_caption("WALI")

    

    font = pygame.font.SysFont(None, 32)

    board = Board(screen)

    p1 = Player(num=1, name='Player One')
    p2 = Player(num=2, name='Player Two')


    # Player 1 always starts
    turn = 1
    
    while True:
        pick_from = gf.check_events()

        # Display Marbles won by each player on the screen.
        winAlertOne = font.render(("P-1 Marbles Won: " + str(board.p1_wins)),
                True, [225,194,194], [0,0,0])

        winAlertTwo = font.render(("P-2 Marbles Won: " + str(board.p1_wins)),
                True, [215,194,194], [0,0,0])

        screen.blit(winAlertOne, [20,636])
        screen.blit(winAlertTwo, [20,20])
        try:

            if turn == 1:
                # Check if game can proceed.
                #gf.can_proceed(board, stats, turn, font, screen, gs)

                alert = font.render("Player One's Turn", True, [255,255,255], gs.bg_color)
                screen.blit(alert, [500, 20])

                if board.board[pick_from-1] == 0:       # Subtraction ensures that input value correlates with python indexing scheme
                    turn = 1
                else:
                    turn = 2
                    gf.get_move(player=p1, pick_from=pick_from, board=board)
                    continue

            elif turn == 2:
                # Check if game can proceed.
                #gf.can_proceed(board, stats, turn, font, screen, gs)
            
                alert = font.render("Player Two's Turn", True, [255,255,255], gs.bg_color)
                screen.blit(alert, [500, 20])

                if board.board[pick_from+5] == 0:       # Addition ensures that input value correlates with python indexing scheme
                    turn = 2
                else:
                    turn = 1
                    gf.get_move(player=p2, pick_from=pick_from, board=board)
                    continue
        except:
            gf.check_events()

        # Update screen with all changes
        gf.update_screen(board, stats)
        pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
