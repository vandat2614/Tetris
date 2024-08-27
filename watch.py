import pygame
from colors import Colors
from time import time

class Watch:
    def __init__(self, position, width, height):
        self.rect = pygame.Rect(position[0], position[1], width, height)

        self.font = pygame.font.SysFont(None, 45)
        self.watch_surface = self.font.render('00:00:00', True, Colors.WHITE)
        self.watch_rect = self.watch_surface.get_rect(center=self.rect.center)

        self.start_time = None
        self.running = False

    def change_time_text(self, time_string='00:00:00'):
        self.watch_surface = self.font.render(time_string, True, Colors.WHITE)
        self.watch_rect = self.watch_surface.get_rect(center=self.rect.center)

    def update(self):
        if self.running:
            elapsed_time = time() - self.start_time
            minutes, seconds = divmod(elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)

            time_string = f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'
            self.change_time_text(time_string)
    
    def draw(self, screen):
        pygame.draw.rect(screen, Colors.LIGHT_BLUE, self.watch_rect, 0, 15)
        screen.blit(self.watch_surface, self.watch_rect)

    def reset(self):
        self.start_time = None
        self.running = False
        self.change_time_text(time_string='00:00:00')

    def start(self):
        if not self.running:
            if not self.start_time:
                self.start_time = time()
            else:
                self.start_time += time() - self.last_time

            self.running = True
            self.update()

    def stop(self):
        if self.running:
            self.running = False
            self.last_time = time()

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.LIGHT_BLUE, self.rect, 0, 15)
        screen.blit(self.watch_surface, self.watch_rect)