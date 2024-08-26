from colors import Colors
from position import Position
import pygame

class Block:
    def __init__(self, id, cell_size):
        self.id = id
        self.states = {}
        self.cell_size = cell_size
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
        self.row_offset = 0
        self.col_offset = 0

    def draw(self, screen, offset_x=11, offset_y=11):
        tiles = self.get_position()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col*self.cell_size+offset_x, tile.row*self.cell_size+offset_y, 
                                        self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(surface=screen, color=self.colors[self.id], rect=tile_rect)

    def move(self, row, col):
        self.row_offset += row
        self.col_offset += col

    def rotate(self):
        self.rotation_state += 1
        self.rotation_state %= 4

    def undo_rotate(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = 3

    def get_position(self):
        tiles = self.states[self.rotation_state]
        movel_tiles = []
        for tile in tiles:
            position = Position(tile.row + self.row_offset, tile.col + self.col_offset)
            movel_tiles.append(position)
        return movel_tiles
    