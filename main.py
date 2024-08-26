import pygame, sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render('Score', True, Colors.WHITE) # more smooth
next_surface = title_font.render('Next', True, Colors.WHITE)
game_over_surface = title_font.render('GAME OVER', True, Colors.WHITE)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode(size=(500, 620))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

game = Game()

AUTO_DOWN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(AUTO_DOWN_UPDATE, 350)

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
                game.update_score(move_down_points=1)
            elif event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            elif event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
        if event.type == AUTO_DOWN_UPDATE and not game.game_over:
            game.move_down()

    score_value_surface = title_font.render(str(game.score), True, Colors.RED)
    screen.fill(Colors.DARK_BLUE)   
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.LIGHT_BLUE, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.LIGHT_BLUE, next_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

