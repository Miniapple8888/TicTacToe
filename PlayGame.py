import pygame
from Helpers import within_boundaries, write, color


def playgame(game):
    # Repainting screen
    game.clear_screen()

    # draw board
    game.draw_board()

    state_text = ""
    replay_text = "Right click to play again!"
    # Check if in terminal state
    state = game.terminal_state()
    if state == 'NO':
        # 1 2 3
        # 4 5 6
        # 7 8 9
        # Events with user input
        # if left click on 1 and case 1 is empty, fill current player
        for i in range(1, 10):
            game.click_square(i)
    else:  # in terminal state
        if state == 'X' or state == 'O':
            state_text = game.winner_text(state)
        if state == 'T':
            # game is a tie
            state_text = "Nobody won."
        # write state text & replay text
        write(game.screen, state_text, 24, color("white"), (165, 617))
        write(game.screen, replay_text, 24, color("white"), (190, 654))
    game.update_board()
