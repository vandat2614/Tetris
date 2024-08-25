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
    
    def reset(self):
        for row in range(self.num_rows):
            self.clear_row(row)

    def is_inside(self, cell):
        if not (0 <= cell.row < self.num_rows and 0 <= cell.col < self.num_cols):
            return False
        return True
    
    def is_empty(self, cell):
        if self.grid[cell.row][cell.col] == 0:
            return True
        return False
    
    def full_row(self, row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0
    
    def move_down(self, row, num_rows):
        for col in range(self.num_cols):
            self.grid[row+num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clear_full_row(self):
        completed = 0
        for row in range(self.num_rows-1, -1, -1):
            if self.full_row(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_down(row, completed)

