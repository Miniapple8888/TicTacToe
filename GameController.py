import pygame
import os
from Helpers import write, color, within_boundaries
from PlayGame import playgame


class Game():

    current_player = "X"
    playtime = 0
    board = [
        '', '', '',
        '', '', '',
        '', '', ''
    ]

    def __init__(self, width, height, fps):

        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(
            (self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        # fills the screen with blackness
    def clear_screen(self):
        self.screen.fill(color("black"))

    # Draw board
    def draw_board(self):
        write(self.screen, "TicTacToe", 64, color("white"), (172, 66))
        # draw rectangle horizontal 1
        pygame.draw.rect(self.screen, color("white"),
                         pygame.Rect(137, 305.47, 365, 7.33))
        # draw rectangle horizontal 2
        pygame.draw.rect(self.screen, color("white"),
                         pygame.Rect(137, 424.81, 365, 7.33))
        # draw rectangle vertical 1
        pygame.draw.rect(self.screen, color("white"),
                         pygame.Rect(250.6, 186, 7.33, 365))
        # draw rectangle vertical 2
        pygame.draw.rect(self.screen, color("white"),
                         pygame.Rect(382, 186, 7.33, 365))
        # Current turn
        current_turn_text = "Current turn: " + self.current_player
        write(self.screen, current_turn_text, 24, color("white"), (175, 580))

    # updates visual interface
    def update_board(self):
        # check each square in the board
        counter = 0
        for s in self.board:
            # if square contains an x or o, draw it
            if s == 'X' or s == 'O':
                square = self.get_square(counter)
                s_x, s_y = square[0], square[1]
                write(self.screen, s, 100, color("white"), (s_x+24, s_y+24))
            counter += 1

        # self-explanatory
    def starting_screen(self):
        self.screen = pygame.Surface(self._display_surf.get_size())
        self.clear_screen()
        self.screen = self.screen.convert()
        self.draw_board()

        # Game mode
    def play(self):
        playgame(self)

        # resets all game values
    def reset(self):
        self.playtime = 0
        self.current_player = 'X'
        self.board = [
            '', '', '',
            '', '', '',
            '', '', ''
        ]

    def toggle_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        elif self.current_player == 'O':
            self.current_player = 'X'

    def get_square(self, index):
        s_x = s_y = s_w = s_h = 0
        if index == 0:
            s_x, s_y, s_w, s_h = 137, 186, 114, 119
        if index == 1:
            s_x, s_y, s_w, s_h = 258, 186, 124, 119
        if index == 2:
            s_x, s_y, s_w, s_h = 389, 186, 113, 119
        if index == 3:
            s_x, s_y, s_w, s_h = 137, 313, 113, 112
        if index == 4:
            s_x, s_y, s_w, s_h = 258, 313, 124, 112
        if index == 5:
            s_x, s_y, s_w, s_h = 389, 313, 113, 112
        if index == 6:
            s_x, s_y, s_w, s_h = 137, 432, 113, 119
        if index == 7:
            s_x, s_y, s_w, s_h = 258, 432, 124, 119
        if index == 8:
            s_x, s_y, s_w, s_h = 389, 432, 113, 119
        return (s_x, s_y, s_w, s_h)

    # Determines which square has been clicked and updates game state accordingly
    def click_square(self, number):
        if self.mouse_click[0]:
            square = self.get_square(number-1)
            s_x, s_y, s_w, s_h = square[0], square[1], square[2], square[3]
            if within_boundaries(self.mouse_pos, s_x, s_y, s_w, s_h) and self.board[number-1] == '':
                self.board[number-1] = self.current_player
                self.toggle_player()

    # checks if game is in a terminal state (X wins, O wins, tie) and returns state
    def terminal_state(self):
        # Check for whether X or O win through each possible case
        # 0
        row1 = self.board[0] == self.board[1] and self.board[1] == self.board[2]
        # 4
        row2 = self.board[3] == self.board[4] and self.board[4] == self.board[5]
        # 8
        row3 = self.board[6] == self.board[7] and self.board[7] == self.board[8]
        # 0
        col1 = self.board[0] == self.board[3] and self.board[3] == self.board[6]
        # 4
        col2 = self.board[1] == self.board[4] and self.board[4] == self.board[7]
        # 8
        col3 = self.board[2] == self.board[5] and self.board[5] == self.board[8]
        # 0
        dia1 = self.board[0] == self.board[4] and self.board[4] == self.board[8]
        # 4
        dia2 = self.board[2] == self.board[4] and self.board[4] == self.board[6]
        player_winning = ''
        if row1 or col1 or dia1:
            player_winning = self.board[0]
        if row2 or col2 or dia2:
            player_winning = self.board[4]
        if row3 or col3:
            player_winning = self.board[8]
        if not player_winning == '':
            return player_winning
        # if board full return T
        tie = True
        for s in self.board:
            # if square is not empty
            if s == '':
                tie = False
        if tie:
            return 'T'
        return 'NO'

    def winner_text(self, winner):
        return 'Player ' + winner + ' wins!'

        # Game execution
    def run(self):

        self.starting_screen()

        # while game is running
        while self._running:

            milliseconds = self.clock.tick(self.fps)
            self.seconds = milliseconds / 1000.0
            self.playtime += self.seconds

            # Quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.K_ESCAPE:
                    self._running = False

                    # get user input
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_click = pygame.mouse.get_pressed()

            self.play()

            # if right click, we reset
            if self.mouse_click[2]:
                self.reset()

                # Renders game
            self._display_surf.blit(self.screen, (0, 0))
            pygame.display.set_caption("FPS: %s" % (self.clock.get_fps()))
            pygame.display.update()
