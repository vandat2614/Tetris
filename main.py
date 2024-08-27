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
next_rect = pygame.Rect(320, 195, 170, 170)

screen = pygame.display.set_mode(size=(500, 620))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

icon = pygame.image.load('Graphics\\icon_in.png')
pygame.display.set_icon(icon)  

game = Game()

AUTO_DOWN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(AUTO_DOWN_UPDATE, 350)


pause_button = Button(position=(320, 568), width=120, height=40)
pause_button.config(text='Pause')
game_pause = False

hand_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
default_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)

volume_button = Button(position=(445, 560), width=50, height=50)
volume_button.config(image_path='Graphics\\volume.png', scale_factor=0.3)
mute = False

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

    score_value_surface = title_font.render(str(game.score), True, Colors.CYAN)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))

    screen.blit(next_surface, (375, 160, 50, 50))
    pygame.draw.rect(screen, Colors.LIGHT_BLUE, next_rect, 0, 10)

    pause_button.draw(screen)
    volume_button.draw(screen, Colors.DARK_BLUE)
    watch.draw(screen)
    watch.update()

    if pause_button.is_hovered() or volume_button.is_hovered():
        pygame.mouse.set_cursor(hand_cursor)
    else: pygame.mouse.set_cursor(default_cursor)

    if game.game_over:
        screen.blit(game_over_surface, (320, 500, 50, 50))
        watch.stop()
        pause_button.config(text='Play again')

    if pause_button.is_clicked():
        if game.game_over:
            pause_button.config(text='Pause')
            game.reset()
            game_pause = False

            watch.reset()
            watch.start()
        else:
            if game_pause:
                pause_button.config(text='Pause')
                watch.start()
            else:
                pause_button.config(text='Continue')
                watch.stop()
            game_pause = not game_pause

    if volume_button.is_clicked():
        mute = not mute
        if mute:
            game.stop_music()
            volume_button.config(image_path='Graphics\\mute.png', scale_factor=0.3)
        else: 
            game.play_music()
            volume_button.config(image_path='Graphics\\volume.png', scale_factor=0.3)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

