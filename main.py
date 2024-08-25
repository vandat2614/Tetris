import pygame, sys
from grid import Grid
# from colors import Colors
from blocks import *

SCREEN_WIDTH, SCREEN_HEIGHT = (300, 600)
FPS = 60

BACKGROUND_COLOR = (27, 16, 156)



screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

NUM_ROWS, NUM_COLS = 20, 10
CELL_SIZE = SCREEN_WIDTH // NUM_COLS

game_grid = Grid(NUM_ROWS, NUM_COLS, CELL_SIZE)
block = SBlock(CELL_SIZE)
block.rotation_state=0
# event handling -> updating positions -> drawing objects
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)   
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

