import pygame, sys
from grid import Grid

SCREEN_WIDTH, SCREEN_HEIGHT = (300, 600)
FPS = 60

BACKGROUND_COLOR = (27, 16, 156)
DARK_GRAY = (26, 31, 40)
GREEN = (47, 230, 23)
RED = (232, 18, 18)
ORANGE = (226, 116, 17)
YELLOW = (237, 234, 4)
PURPLE = (166, 0, 247)
CYAN = (21, 204, 209)
BLUE = (13, 64, 216)

CELL_COLORS = [DARK_GRAY, GREEN, RED, ORANGE, YELLOW, PURPLE, CYAN, BLUE]


screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

NUM_ROWS, NUM_COLS = 20, 10
CELL_SIZE = SCREEN_WIDTH // NUM_COLS

game_grid = Grid(NUM_ROWS, NUM_COLS, CELL_SIZE, CELL_COLORS)


# event handling -> updating positions -> drawing objects
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)   
    game_grid.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

