from colors import Colors
import pygame

class Block:
    def __init__(self, id, cell_size):
        self.id = id
        self.states = {}
        self.cell_size = cell_size
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def draw(self, screen):
        tiles = self.states[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col*self.cell_size+1, tile.row*self.cell_size+1, 
                                        self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(surface=screen, color=self.colors[self.id], rect=tile_rect)