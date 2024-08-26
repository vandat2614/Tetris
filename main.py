import pygame, sys
from game import Game
from colors import Colors
from button import Button
from watch import Watch

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render('Score', True, Colors.WHITE) # more smooth
next_surface = title_font.render('Next', True, Colors.WHITE)
game_over_surface = title_font.render('GAME OVER', True, Colors.WHITE)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 195, 170, 180)

screen = pygame.display.set_mode(size=(500, 620))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

game = Game()

AUTO_DOWN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(AUTO_DOWN_UPDATE, 350)

exit_button = Button(text='Exit', position=(410, 570), width=90, height=40)
pause_button = Button(text='Pause', position=(310, 570), width=95, height=40)

game_pause = False

hand_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
default_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)

watch = Watch((320, 400), width=170, height=50)
watch.start()

# event handling -> updating positions -> drawing objects
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.reset()
                watch.reset()
                watch.start()
            
            if not game.game_over and not game_pause:
                if event.key == pygame.K_UP:
                    game.rotate()
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(move_down_points=1)
                elif event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
    
        if event.type == AUTO_DOWN_UPDATE and not game.game_over and not game_pause:
            game.move_down()

    screen.fill(Colors.DARK_BLUE)   

    screen.blit(score_surface, (365, 20, 50, 50))
    pygame.draw.rect(screen, Colors.LIGHT_BLUE, score_rect, 0, 10)

    score_value_surface = title_font.render(str(game.score), True, Colors.RED)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))

    screen.blit(next_surface, (375, 160, 50, 50))
    pygame.draw.rect(screen, Colors.LIGHT_BLUE, next_rect, 0, 10)

    pause_button.draw(screen)
    exit_button.draw(screen)
    watch.draw(screen)
    watch.update()

    if game.game_over:
        screen.blit(game_over_surface, (320, 500, 50, 50))
        watch.stop()

    if exit_button.is_hovered() or pause_button.is_hovered():
        pygame.mouse.set_cursor(hand_cursor)
    else: pygame.mouse.set_cursor(default_cursor)


    if exit_button.is_clicked():
        pygame.quit()
        sys.exit()

    if pause_button.is_clicked():
        if game_pause:
            pause_button.change_text('Pause')
            watch.start()
        else:
            pause_button.change_text('Continue')
            watch.stop()
        game_pause = not game_pause

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

