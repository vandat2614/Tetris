import pygame
from colors import Colors

class  Grid:
    def __init__(self, num_rows, num_cols, cell_size):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.grid = [[0] * num_cols for _ in range(num_rows)]
        self.cell_colors = Colors.get_cell_colors()

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size+1, row*self.cell_size+1, 
                                        self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(surface=screen, color=self.cell_colors[cell_value], rect=cell_rect)

    def is_inside(self, cell):
        if not (0 <= cell.row < self.num_rows and 0 <= cell.col < self.num_cols):
            return False
        return True