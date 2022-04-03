# handles the actual game

import pygame
from checkers.board import Board
from .constants import RED, WHITE

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def reset(self):
        self._init()
    
    # if you select something, this method will be called
    # it gives you option during the game when you select a piece
    # it handels
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col) #try to move the selected piece to the passed row and column
            if not result: # if that is not possible or makes no sense:
                self.selected = None # selected is reset and select will be re-called until the result move is valid
                self.select(row, col)
        piece = self.board.get_piece(row, col)

        # if the selection was valid, return true, else return false
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
    
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            # move the piece
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        
        return True

    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED