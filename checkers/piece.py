from pickle import TRUE
import pygame
from .constants import GREY, WHITE, SQUARE_SIZE, CROWN

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    # calculate the postion of the piece based on the row and column that it is in
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    # change king variable
    def make_king(self):
        self.king = True
    
    #draw the piece itself
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        # draw two circles, the bigger one is the padding and the smaler one is on top
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos() 

    def __repr__(self):
        return str(self.color)
