import pygame
from checkers.constants import SQUARE_SIZE, WIDTH, HEIGHT, RED
from checkers.game import Game

FPS = 60 #max frames per second

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = int(y / SQUARE_SIZE)
    col = int(x / SQUARE_SIZE)
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        
        game.update()
        
    pygame.quit()
    
main()