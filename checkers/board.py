# this class represents the checkers board

import pygame
from .constants import BLACK, WHITE, ROWS, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12 # how many red and white pieces we have, 12 each
        self.red_kings = self.white_kings = 0 # how many king peaces each side has, at the start 0

    #definition to draw the board  
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range (ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
