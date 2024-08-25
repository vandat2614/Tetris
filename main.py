import pygame, sys
from game import Game

SCREEN_WIDTH, SCREEN_HEIGHT = (300, 600)
FPS = 60
BACKGROUND_COLOR = (27, 16, 156)
NUM_ROWS, NUM_COLS = 20, 10
CELL_SIZE = SCREEN_WIDTH // NUM_COLS
MOVE_DOWN_DELAY = 200


screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

game = Game(NUM_ROWS, NUM_COLS, CELL_SIZE)

AUTO_DOWN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(AUTO_DOWN_UPDATE, MOVE_DOWN_DELAY)

# event handling -> updating positions -> drawing objects
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
            elif event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
            elif event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            elif event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
        if event.type == AUTO_DOWN_UPDATE and not game.game_over:
            game.move_down()

    screen.fill(BACKGROUND_COLOR)   
    game.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

