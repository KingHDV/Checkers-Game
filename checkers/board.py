# this class represents the checkers board
import pygame
from .constants import BLACK, WHITE, RED, ROWS, COLS, SQUARE_SIZE
from .piece import Piece
class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12 # how many red and white pieces we have, 12 each
        self.red_kings = self.white_kings = 0 # how many king peaces each side has, at the start 0
        self.create_board()

    #definition to draw the board  
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range (ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        # easy way to swap things in a list, put it in reverse
        # self.board[piece.row][piece.col] moves to self.board[row][col] and vice versa
        # this means the piece moves to a place and the empty slot also moves
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col] 
        piece.move(row, col)

        #make sure if the piece becomes a king when hitting the first or last row
        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    #draw the square and all the pieces
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)