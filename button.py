import pygame
from colors import Colors

class Button:
    def __init__(self, text, position, width, height):        
        self.rect = pygame.Rect(position[0], position[1], width, height)
        
        self.font = pygame.font.SysFont(None, 30)
        self.text_surface = self.font.render(text, True, Colors.WHITE)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

        self.pressed = False

    def change_text(self, new_text):
        self.text_surface = self.font.render(new_text, True, Colors.WHITE)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.LIGHT_BLUE, self.rect, 0, 15)
        # pygame.draw.rect(screen, Colors.BLACK, self.rect, 2, 10)
        screen.blit(self.text_surface, self.text_rect)
        
    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos): 
            if mouse_pressed and not self.pressed:
                self.pressed = True
                return True

        if not mouse_pressed:
            self.pressed = False 

        return False 

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)