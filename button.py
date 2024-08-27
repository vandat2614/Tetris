import pygame
from colors import Colors

class Button:
    def __init__(self, position, width, height):        
        self.rect = pygame.Rect(position[0], position[1], width, height)
        self.pressed = False

    def config(self, text='', image_path=None, scale_factor=1):
        if image_path == None:
            self.font = pygame.font.SysFont(None, 30)
            self.surface = self.font.render(text, True, Colors.WHITE)
            self.surface_rect = self.surface.get_rect(center=self.rect.center) 
        else:
            image = pygame.image.load(image_path).convert_alpha()
            self.surface = self.scale_image(image, scale_factor)
            self.surface_rect = self.surface.get_rect(center=self.rect.center)

    def scale_image(self, image, scale_factor=1):
        original_width = image.get_width()
        original_height = image.get_height()

        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        return pygame.transform.smoothscale(image, (new_width, new_height))

    def draw(self, screen, bg=Colors.LIGHT_BLUE):
        pygame.draw.rect(screen, bg, self.rect, 0, 15)
        # pygame.draw.rect(screen, Colors.BLACK, self.rect, 2, 10)
        screen.blit(self.surface, self.surface_rect)
        
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