import pygame
from .constansts import RED, WHITE, SQUARE_SIZE, GREY, crown 




class Piece:
    PADDING = 15 
    OUTLINE = 2

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king(self):
        self.king = True 

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING 
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)
        if self.king:
            win.blit(crown, (self.x - crown.get_width()//2, self.y - crown.get_height()))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.colour)