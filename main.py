import pygame, sys

SCREEN_WIDTH, SCREEN_HEIGHT = (300, 600)
FPS = 60

BACKGROUND_COLOR = (27, 16, 156)


screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)   
    pygame.display.update()
    clock.tick(FPS)

