import sys
import pygame
import numpy as np

pygame.init()

#Display Constant Color
WHITE = (225, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (180, 180, 180)

#Sizes and Proportions
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.displayset_caption("Tic Tac Toe AI")
screen.fill(BLACK)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines(color=WHITE):
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, color, start_pos=(0, SQUARE_SIZE*i), end_pos=(WIDTH, SQUARE_SIZE * i), width=LINE_WIDTH)
        pygame.draw.line(screen, color, start_pos=(SQUARE_SIZE*i, 0), end_pos=(SQUARE_SIZE * i, HEIGHT), width=LINE_WIDTH)

    