import pygame, sys
from game import Game

SCREEN_WIDTH, SCREEN_HEIGHT = (300, 600)
FPS = 60
BACKGROUND_COLOR = (27, 16, 156)
NUM_ROWS, NUM_COLS = 20, 10
CELL_SIZE = SCREEN_WIDTH // NUM_COLS


screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

game = Game(NUM_ROWS, NUM_COLS, CELL_SIZE)

# event handling -> updating positions -> drawing objects
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            elif event.key == pygame.K_DOWN:
                game.move_down()
            elif event.key == pygame.K_LEFT:
                game.move_left()
            elif event.key == pygame.K_RIGHT:
                game.move_right()

    screen.fill(BACKGROUND_COLOR)   
    game.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

