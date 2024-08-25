import random
from grid import Grid
from blocks import *

class Game:
    def __init__(self, num_rows, num_cols, cell_size):
        self.grid = Grid(num_rows, num_cols, cell_size)
        self.cell_size = cell_size
        self.blocks = []
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False

    def reset_blocks(self):
        self.blocks = [IBlock(self.cell_size), JBlock(self.cell_size), LBlock(self.cell_size), OBlock(self.cell_size), SBlock(self.cell_size), TBlock(self.cell_size), ZBlock(self.cell_size)]

    def get_random_block(self):
        if len(self.blocks) == 0: self.reset_blocks()
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

    def reset(self):
        self.grid.reset()
        self.reset_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside():
            self.current_block.move(0, 1)
        if self.collision():
            self.lock_block()

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside():
            self.current_block.move(0, -1)
        if self.collision():
            self.lock_block()

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or self.collision():
            self.current_block.move(-1, 0)
            self.lock_block()

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside():
            self.current_block.undo_rotate()
        if self.collision():
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_position()
        for tile in tiles:
            self.grid.grid[tile.row][tile.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full_row()

        if not self.block_inside() or self.collision():
            self.game_over = True

    def block_inside(self):
        tiles = self.current_block.get_position()
        for tile in tiles:
            if not self.grid.is_inside(tile):
                return False
        return True
    
    def collision(self):
        tiles = self.current_block.get_position()
        for tile in tiles:
            if not self.grid.is_empty(tile):
                return True
        return False
